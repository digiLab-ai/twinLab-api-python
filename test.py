import time
from pprint import pprint

import examples.api as api

dataset_path = "resources/datasets/pollution.csv"
dataset_id = "pollution"
model_path = "resources/campaigns/pollution/parameters.json"
model_id = "pollution-model"
predict_path = "resources/campaigns/pollution/eval.csv"
processor = "cpu"

response = api.get_user()
pprint(response)

response = api.get_versions()
pprint(response)

response = api.list_datasets()
pprint(response)

response = api.upload_dataset(dataset_path, dataset_id)
pprint(response)

response = api.list_datasets()
pprint(response)

response = api.view_dataset(dataset_id)
pprint(response)

response = api.summarise_dataset(dataset_id)
pprint(response)

response = api.list_models()
pprint(response)

response = api.train_model(model_path, model_id, processor)
pprint(response)

response = api.status_model(model_id)
pprint(response)

# Allow time for the model to train
time.sleep(10)

response = api.status_model(model_id)
pprint(response)

response = api.list_models()
pprint(response)

response = api.summarise_model(model_id)
pprint(response)

response = api.use_model(
    predict_path, model_id, "predict", processor)
pprint(response)

response = api.delete_model(model_id)
pprint(response)

response = api.list_models()
pprint(response)

response = api.delete_dataset(dataset_id)
pprint(response)

response = api.list_datasets()
pprint(response)
