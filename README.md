# How different prompts impact health answer correctness

Code, results and data for "Dr ChatGPT tell me what I want to hear: How different prompts impact health answer correctness" EMNLP 2023


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


