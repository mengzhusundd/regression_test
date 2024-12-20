# regression_test

# Golden Dataset is ready to use in golden_dataset.json!

## This repository is also a very simple tool to generate more baseline data in the golden dataset

1. git clone this repository to your local 
2. `cd` to your `regression_test` directory, run `python get_sql.py`to generate sql for MODE
3. In MODE Snowflake database, run the generated SQL, export the results to local as a csv file
4. Still under `regression_test` repository, run `python convert.py` to convert the csv file dump into a json format golden dataset
5. copy - paste the generated golden dataset into runtime file 

## Notes
* There are currently 41 available examples in the golden dataset as for 12/20/2024
