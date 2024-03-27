"""
Read results from ChatGPT health misinformation experiments and put them in single results file.
"""

import argparse
import logging
import csv
import os
import re
import xmltodict
import pandas as pd
from tabulate import tabulate

logging.basicConfig()
logger = logging.getLogger(__name__)
logger.setLevel(level=logging.INFO)


def get_answer_type(answer: str) -> str:
    answer = answer.lower()
    answer = re.sub('[^a-z]*', '', answer)
    answer = re.sub('^theansweris', '', answer)
    answer = answer[0:2]
    match answer:
        case 'ye':
            return "Yes"
        case 'no':
            return "No"
        case 'im':
            return "Unsure"
        case 'un':
            return "Unsure"
        case _:
            return "Unsure"


def get_answer_type_trec(topic: str) -> str:
    answer = topic.get('stance', topic.get('answer', ''))
    match answer:
        case 'helpful':
            return "Yes"
        case 'yes':
            return "Yes"
        case 'unhelpful':
            return "No"
        case 'no':
            return "No"
        case _:
            return "Unsure"


def clean_answer(answer: str) -> str:
    return re.sub('\n', ' ', answer)


def read_topics(topic_files=['../../data/misinfo-resources-2021/topics/misinfo-2022-topics.xml',
                             '../../data/misinfo-resources-2021/topics/misinfo-2021-topics.xml']) -> dict:
    """
    Read Qrels from multiple TREC topic XML file.
    :param topic_files: list of topic filenames
    :return: dictionary qid -> ["yes"|"no"|"unsure"]
    """
    topics = {}
    for topic_file in topic_files:
        topics.update(read_topic_file(topic_file))
    return topics


def read_topic_file(topic_file) -> dict:
    """
    Read Qrels from TREC topic XML file.
    :param topic_file: topic filename
    :return: dictionary qid -> ["yes"|"no"|"unsure"]
    """
    with open(topic_file) as xml_file:
        json_doc = xmltodict.parse(xml_file.read(), xml_attribs=False)
        return {topic['number']: get_answer_type_trec(topic) for topic in json_doc['topics']['topic']}


def eval_answer_correctness(df: pd.DataFrame, correct_column='Correct', answer_column='ChatGPTAnswer') -> dict:
    """
    Computes evaluation measures from the supplied results.
    :param answer_column: name of column containing ChatGPT column
    :param correct_column: name of column that captures correctness
    :param df: Dataframe of individual topic results
    :return: Dictionary with keys as measure names and values as, well, values.
    """
    correct = len([row for row in df.iterrows() if row[1][correct_column]])
    unsure = len([row for row in df.iterrows() if row[1][answer_column] == "Unsure"])
    total = len(df.index)
    logger.info(f"{correct} / {total} correct = {correct / total}")
    return {"Correct": correct, "Unsure": unsure, "Incorrect": total - correct - unsure, "Total": total,
            "Accuracy": correct / total}


def eval_answer_correctness_df(df: pd.DataFrame, correct_column='Correct', answer_column='ChatGPTAnswer') -> pd.DataFrame:
    """
    Computes evaluation measures from the supplied results.
    :param df: Dataframe of individual topic results
    :return: Dataframe with columns ["measure', "value"]
    """
    eval_results = eval_answer_correctness(df, correct_column, answer_column)
    return pd.DataFrame({'measure': eval_results.keys(), 'value': eval_results.values()})


def read_results_csv(csv_files, topics=read_topics(), label="") -> pd.DataFrame:
    """
    Process the supplied CSV files into Dataframe of results
    :param csv_files: list of CSV files
    :param topics: list of TREC topic files
    :return: Dataframe with one row per topic per file.
    """
    results = []
    for csv_file in csv_files:
        logger.info(f"Reading {csv_file}")
        with open(csv_file, newline='') as csvfile:
            reader = csv.reader((line.replace('\0', '') for line in csvfile), delimiter=',', quotechar='"')
            next(reader)  # skip header row
            for count, row in enumerate(reader):
                qid, question, answer = row[0:3]
                stance = row[3] if len(row) > 3 else "N/A"
                qid = re.sub('[^0-9]*', '', qid)
                ground_truth = topics.get(qid, 'NA')
                chatgpt_answer = get_answer_type(answer)
                results.append(
                    [
                        label,
                        os.path.basename(csv_file),
                        qid, question,
                        ground_truth,
                        chatgpt_answer,
                        ground_truth == chatgpt_answer,
                        stance,
                        clean_answer(answer)
                    ]
                )
    return pd.DataFrame(results,
                        columns=['Label',
                                 'File',
                                 'QueryId',
                                 'Question',
                                 'GroundTruth',
                                 'ChatGPTAnswer',
                                 'Correct',
                                 'Stance',
                                 'GPTText']
                        )


if __name__ == '__main__':
    argparser = argparse.ArgumentParser(description="Misinformation experiment analysis.",
                                        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    argparser.add_argument('-v', '--verbose', action='store_true', help="Turn on verbose logging.")
    argparser.add_argument('--latex', action='store_true', help="Output tables in latex.")
    argparser.add_argument('--no_trim', action='store_true', help="Don't trim print output of ChatGPT text.")
    argparser.add_argument('result_csvs', nargs="+", help="One or more CSV results files")
    argparser.add_argument('--topics', nargs="+",
                           default=['../../data/misinfo-resources-2021/topics/misinfo-2022-topics.xml',
                                    '../../data/misinfo-resources-2021/topics/misinfo-2021-topics.xml'],
                           help="One or more CSV results files")

    args = argparser.parse_args()

    df = read_results_csv(args.result_csvs, topics=read_topics(args.topics))

    if not args.no_trim:
        df['GPTText'] = [text[0:30] for text in df['GPTText']]  # trim long text

    table_fmt = 'latex' if args.latex else 'psql'
    print(tabulate(df, headers='keys', tablefmt=table_fmt, showindex="never"))
    print(tabulate(eval_answer_correctness_df(df), headers='keys', tablefmt=table_fmt, showindex="never"))
