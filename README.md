# How different prompts impact health answer correctness

Code, results and data for our paper:

[Dr ChatGPT tell me what I want to hear: How different prompts impact health answer correctness](https://aclanthology.org/2023.emnlp-main.928/) EMNLP 2023

```bibtex
@inproceedings{koopman-zuccon-2023-dr,
    title = "Dr {C}hat{GPT} tell me what {I} want to hear: How different prompts impact health answer correctness",
    author = "Koopman, Bevan  and
      Zuccon, Guido",
    editor = "Bouamor, Houda  and
      Pino, Juan  and
      Bali, Kalika",
    booktitle = "Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing",
    month = dec,
    year = "2023",
    address = "Singapore",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2023.emnlp-main.928",
    doi = "10.18653/v1/2023.emnlp-main.928",
    pages = "15012--15022"
}
```


## Results


### Main Results
List of result files:

- Yes/No:
	- `misinfo-answers-2021-yesno-run1.csv`: TREC 2021 results (50 topics) obtained with prompt containing direct question and yes/no instruction

	- `misinfo-answers-2022-yesno-run1.csv`: TREC 2022 results (50 topics) obtained with prompt containing direct question and yes/no instruction

	- `misinfo-answers-2021-yesno-with-passages-run1.csv`: TREC 2021 results for questions with passages as prompts (35 topics). Prompt has yes/no instruction. Assignation has been done manually

- Yes/No/Unsure:
	- `misinfo-answers-2021-yesnounsure-run1.csv`: TREC 2021 results (50 topics) obtained with prompt containing direct question and yes/no/unsure instruction

	- `misinfo-answers-2022-yesnounsure-run1.csv`: TREC 2022 results (50 topics) obtained with prompt containing direct question and yes/no/unsure instruction

	- `misinfo-answers-2021-yesnounsure-with-passages-run1.csv`: TREC 2021 results for questions with passages as prompts (35 topics). Prompt has yes/no/unsure instruction. Assignation has been done manually

### Reverse Polarity Results

Questions in the TREC Misinformation dataset are in the form "Can X treat Y?".

Our initial results, discussed below, revealed a systematic bias in ChatGPT behaviour dependent on whether the ground truth was a Yes or No answer. 

To further investigate this effect we conducted an additional experiment whereby we manually rephrased each question to its reversed form: "Can X treat Y?" becomes "X can't treat Y?".

List of results files:

- Yes/No
	- `misinfo-answers-2021-yesno-reversed-polarity.csv`: TREC 2021 results (50 topics) obtained with prompt containing direct question and yes/no instruction.
	- `misinfo-answers-2022-yesno-reversed-polarity.csv`: TREC 2022 results (50 topics) obtained with prompt containing direct question and yes/no instruction


- Yes/No/Unsure

	- `misinfo-answers-2021-yesnounsure-reversed-polarity.csv`: TREC 2021 results (50 topics) obtained with prompt containing direct question and yes/no/unsure instruction
	- `misinfo-answers-2022-yesnounsure-reversed-polarity.csv`: TREC 2022 results (50 topics) obtained with prompt containing direct question and yes/no/unsure instruction

## Analysis

The [analysis](./analysis) folder contains scripts and a notebook for the analysis of the results and the creation of all the plots used for the paper and presestion. It has its own [README.md](./analysis/README.md).
