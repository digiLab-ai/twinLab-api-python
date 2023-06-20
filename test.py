import time
from pprint import pprint

import api

dataset_path = "resources/datasets/pollution.csv"
dataset_id = "pollution"
campaign_path = "resources/campaigns/pollution/parameters.json"
campaign_id = "pollution-campaign"
predict_path = "resources/campaign/pollution/eval.csv"
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

response = api.list_campaigns()
pprint(response)

response = api.train_campaign(campaign_path, campaign_id, processor)
pprint(response)

response = api.status_campaign(campaign_id)
pprint(response)

# Allow time for the campaign to train
time.sleep(10)

response = api.status_campaign(campaign_id)
pprint(response)

response = api.list_campaigns()
pprint(response)

response = api.summarise_campaign(campaign_id)
pprint(response)

response = api.use_campaign(
    predict_path, campaign_id, "predict", processor)
pprint(response)

response = api.delete_campaign(campaign_id)
pprint(response)

response = api.list_campaigns()
pprint(response)

response = api.delete_dataset(dataset_id)
pprint(response)

response = api.list_datasets()
pprint(response)
