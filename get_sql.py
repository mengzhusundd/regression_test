import json
import os


# getting a list of all delivery uuids from Ani's prepared golden dataset to query results in MODE 
deliveries = []

def getDeliveriesFromJson(): 
  input_file_path = "golden_dataset_ani_version.json"

  with open(input_file_path, "r") as file:
      # Parse the JSON string into a Python dictionary
      data = json.load(file)

      # Access the 'golden_dataset' array
      golden_dataset = data["golden_dataset"][0]

      # Extract all deliveries from the 'golden_dataset' array
      for deliveryUuid in golden_dataset:
          deliveries.append(deliveryUuid)

      print("Extracted deliveryUUIDs:")
      print(deliveries)
      return deliveries


# get a list of delivery uuids from Argil dataset to query results in MODE
def getDeliveriesFromDirectory():
   argil_file_path = "/Users/zoey.sun/Projects/argil/models/argil-nv-receipt-ocr/data/edge_cases/audit_2024-06-10"
   delivery_files = os.listdir(argil_file_path)
   result = [file.split(".")[0] for file in delivery_files if file.endswith(".json")]
   print(result)
   return result
deliveries = getDeliveriesFromDirectory()



# Prepare the SQL in MODE
deliveries_str = str(tuple(deliveries))
sql = """
SELECT
  a.PREDICTION_RESULT AS prediction_result
FROM
  IGUAZU.SERVER_EVENTS_PRODUCTION.ARGIL_PREDICTION_LOGGING AS a
  JOIN IGUAZU.MERCHANT.RECEIPT_UPDATE_EVENT AS b ON a.PREDICTION_FEATURES [0] :value = b.DELIVERY_UUID
WHERE
  b.DELIVERY_UUID IN {};

""".format(deliveries_str)
print("SQL to put in MODE")
print(sql)