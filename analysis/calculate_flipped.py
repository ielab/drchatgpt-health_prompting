"""
RQ2 - Evidence Biased Evaluation. Compares the output of RQ1 and RQ2 to work out how many questions changed correctness.
"""

import argparse
import logging
import pandas as pd
from tabulate import tabulate
from extract_experimental_results import read_results_csv, eval_answer_correctness_df

logging.basicConfig()
logger = logging.getLogger(__name__)
logger.setLevel(level=logging.INFO)


def determine_change_status(rq1_prediction, rq2_prediction):
    if rq1_prediction == rq2_prediction:
        return 'Unchanged'
    elif rq2_prediction == "Unsure":
        return "Unsure"
    else:
        return "Flipped"


def write_results_to_csv(csv_results_file, df: pd.DataFrame):
    df.to_csv(csv_results_file)
    logger.info(f"Results written to {csv_results_file}.")


def calc_flipped_totals(df: pd.DataFrame):
    return df.groupby(by=["Change Status", "Correct_rq2"], as_index=False)['ChatGPTAnswer_rq2'].count()


def calculate_flipped(rq1_result_csvs, rq2_result_csvs, label=""):
    rq1_results = read_results_csv(rq1_result_csvs, label=label)
    rq1_results = rq1_results.drop(columns=['GPTText'])
    rq2_results = read_results_csv(rq2_result_csvs, label=label)
    rq2_results = rq2_results.drop(columns=['GroundTruth', 'GPTText'])

    all_results = rq1_results.merge(rq2_results, on=['QueryId'], how='inner', suffixes=["_rq1", "_rq2"])
    all_results['Change Status'] = [
        determine_change_status(row[1]['ChatGPTAnswer_rq1'], row[1]['ChatGPTAnswer_rq2'])
        for row in all_results.iterrows()]

    return all_results


if __name__ == '__main__':
    argparser = argparse.ArgumentParser(description="Misinformation experiment analysis for RQ2.",
                                        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    argparser.add_argument('--rq1_result_csvs', nargs="+", required=True, help="One or more CSV results files")
    argparser.add_argument('--rq2_result_csvs', nargs="+", required=True, help="One or more CSV results files")
    argparser.add_argument('--topics', nargs="+",
                           default=['../../data/misinfo-resources-2021/topics/misinfo-2022-topics.xml',
                                    '../../data/misinfo-resources-2021/topics/misinfo-2021-topics.xml'],
                           help="One or more CSV results files")
    argparser.add_argument('--latex', action='store_true', help="Output tables in latex.")
    argparser.add_argument('-o', '--output_to_csv', help="Output all results to CSV.")
    args = argparser.parse_args()

    all_results = calculate_flipped(args.rq1_result_csvs, args.rq2_result_csvs)
    if args.output_to_csv:
        write_results_to_csv(args.output_to_csv, all_results)

    table_fmt = 'latex' if args.latex else 'psql'
    print(tabulate(all_results, headers='keys'))
    print(tabulate(
        eval_answer_correctness_df(all_results, correct_column='Correct_rq2', answer_column='ChatGPTAnswer_rq2'),
        headers='keys', tablefmt=table_fmt, showindex="never"))
    print(tabulate(calc_flipped_totals(all_results), headers='keys', tablefmt=table_fmt, showindex="never"))  # .transform(lambda x: x/x.sum()))
