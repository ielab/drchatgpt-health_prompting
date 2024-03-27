# Health Misinformation Analysis

## FIles

These files contain some code/scripts for interpretting results, including generating plots:

| File      | Description |
| ----------- | ----------- |
| `SankeyDiagram.Rmd` | R Markdown file that creates the Sankey diagram for the paper (reads `all_flipped_results.csv`)
| `health-misinformation.Rproj` | R project associated with `SankeyDiagram.Rmd`
| `MisinfomationResultsAnalysis.ipynb` | Jupyter Notebook for creating paper plots (and other small analysis)
| `Pipfile` | Pipfile for dependecies (run `pipenv shell` to create a shell with everything)
| `README.md` | This file.
| `all_flipped_results.csv` | Extract of all results for use by `SankeyDiagram.Rmd`. Extract was done by `calculate_flipped.py`
| `calculate_flipped.py` | Used for RQ2. Compares the output of RQ1 and RQ2 to work out how many questions changed correctness.
| `extract_experimental_results.py` | Used for RQ1 Read results from ChatGPT health misinformation experiments and put them in single results file.

## RQ1 Scripts

```
usage: extract_experimental_results.py [-h] [-v] [--latex] [--no_trim] [--topics TOPICS [TOPICS ...]] result_csvs [result_csvs ...]

Misinformation experiment analysis.

positional arguments:
  result_csvs           One or more CSV results files

options:
  -h, --help            show this help message and exit
  -v, --verbose         Turn on verbose logging. (default: False)
  --latex               Output tables in latex. (default: False)
  --no_trim             Don't trim print output of ChatGPT text. (default: False)
  --topics TOPICS [TOPICS ...]
                        One or more CSV results files (default: ['../../data/misinfo-resources-2021/topics/misinfo-2022-topics.xml', '../../data/misinfo-
                        resources-2021/topics/misinfo-2021-topics.xml'])
```


## RQ2 Scripts

```
usage: calculate_flipped.py [-h] --rq1_result_csvs RQ1_RESULT_CSVS [RQ1_RESULT_CSVS ...] --rq2_result_csvs RQ2_RESULT_CSVS [RQ2_RESULT_CSVS ...] [--topics TOPICS [TOPICS ...]]
                            [--latex] [-o OUTPUT_TO_CSV]

Misinformation experiment analysis for RQ2.

options:
  -h, --help            show this help message and exit
  --rq1_result_csvs RQ1_RESULT_CSVS [RQ1_RESULT_CSVS ...]
                        One or more CSV results files (default: None)
  --rq2_result_csvs RQ2_RESULT_CSVS [RQ2_RESULT_CSVS ...]
                        One or more CSV results files (default: None)
  --topics TOPICS [TOPICS ...]
                        One or more CSV results files (default: ['../../data/misinfo-resources-2021/topics/misinfo-2022-topics.xml', '../../data/misinfo-
                        resources-2021/topics/misinfo-2021-topics.xml'])
  --latex               Output tables in latex. (default: False)
  -o OUTPUT_TO_CSV, --output_to_csv OUTPUT_TO_CSV
                        Output all results to CSV. (default: None)
                        
```


## Reproducing

`MisinfomationResultsAnalysis.ipynb` will show step by step how the above two scripts use contents from `/results/health-misinformation` to get all our results.