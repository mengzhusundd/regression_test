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

rest_of_deliveries = [
  "ccfea2f0-8eca-3001-8b0d-db6debc2c5f5",
  "ac578fe4-6727-3001-b4e1-704574a3f9b8",
  "8553b7d5-5d2b-3001-9e7e-21a07540641d",
  "a6746ce2-bdb5-3001-9008-8e83f598442a",
  "08aacc25-9280-3001-88ba-32e503cbca0f",
  "02f5d210-8e68-3001-a57f-ee8942a2ad61",
  "a58b9428-e5d7-3001-ace0-127fad70fa06",
  "8779d37b-9f5a-3001-865b-33d6f4f7f3e7",
  "f0c9f949-3e91-3001-9cb3-3f1ba1c507b8",
  "7094d756-3c34-3001-b68f-d48981105042",
  "05d2f5d2-7f30-3001-b42a-0ce9cff5d4ec",
  "0ed8b395-04bd-3001-a042-34e55fe3ab6a",
  "f6c7b8dd-f26b-3001-b2f7-177148d9342c",
  "9141eaea-f5a4-3001-9e46-b0ac5505f975",
  "c2d79797-1f69-3001-aa42-be1aea33bdc3",
  "8c637a5a-d7c7-3001-b35a-90481029235b",
  "865f2c73-986d-3001-8248-e28bbb93d781",
  "758e38d8-87a1-3001-8243-1c628a3feb0d",
  "f14ef40e-1f14-3001-8fc6-7ec514d126e7",
  "0ad6fd72-6c98-3001-a5dc-9642b7f0535a",
  "71b1b631-041d-3001-9053-0a14562ce921",
  "6f709763-3f3a-3001-81f1-15ffc4da2031",
  "6c2630e1-d325-3001-b0fc-82bf0d121189",
  "96e1b81e-c1e4-3001-b7c4-87592cbc6ee3",
  "5db1ed12-c6db-3001-8d9c-afdedc731ecb",
  "1d999aad-0392-3001-b1d8-4d2b080c73a1",
  "65921f68-237e-3001-bc9b-5ef3877c801e",
  "f0c4bf0c-8bae-3001-ae76-975ee6ad8c00",
  "a216d7df-c38d-3001-b33d-702d7938c922"
]



# Prepare the SQL in MODE
deliveries_str = str(tuple(rest_of_deliveries))
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