# goal: convert csv file to a json file 

# read in csv file 
import pandas as pd
import json

class MonetaryData:
    def __init__(self, unitAmount = None, currency = None, displayString = None, decimalPlace = None):
        self.unitAmount = unitAmount
        self.currency = currency
        self.displayString = displayString
        self.decimalPlace = decimalPlace

file_name = "query_result.csv"

data_frame = pd.read_csv(file_name)
for raw_result in data_frame['PREDICTION_RESULT']:

    json_result = json.loads(raw_result)
    result_str = ["" for i in range (10)]
    for item in json_result:
        value = item['value']
        if item['key'] == 'delivery_uuid':
            result_str[0] = "delivery_uuid is: {} \n".format(value)
        # total amount is the same thing as grand total 
        if item['key'] == 'total_amount':
            result_str[1] = "grand_total is: {} \n".format(value)
        if item['key'] == 'subtotal_amount':
            result_str[2] = "subtotal_amount is: {}".format(value)
        if item['key'] == 'tax_amount':
            result_str[3] = "tax_amount: {}".format(value)
        if item['key'] == 'matched_item_info':
            result_str[4] = "matched_item is: {}".format(value)
        if item['key'] == 'unmatched_item_info':
            result_str[5] = "unmatched_item_info: {}".format(value)
        if item['key'] == 'bag_fee_info':
            result_str[6] = "bag_fee: {}".format(value)
        if item['key'] == 'bottle_fee_info':
            result_str[7] = "bottle_fee: {}".format(value)
        if item['key'] == 'confidence_score':
            result_str[8] = "confidence_score: {}".format(value)
        if item['key'] == 'is_legible':
            result_str[9] = "is_legible: {}".format(value)
    for elm in result_str:
        print(elm)
        print()
    print("============ NEXT DELIVERY =============")