# regression_test: golden dataset generate manual

This is a very simple tool to generate golden dataset

1. Use get_sql.py to generate sql to run in MODE
2. In MODE Snowflake database, run the generated SQL, export the results to local as a csv file
3. Use convert.py to convert the csv file dump into a json format golden dataset that we want
4. copy - paste the generated golden dataset into runtime file 

