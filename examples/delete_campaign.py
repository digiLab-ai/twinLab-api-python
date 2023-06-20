import json
import sys

from api import delete_campaign


if len(sys.argv) != 2:
    print(f"Usage: python {sys.argv[0]} <campaign_id>")
    exit()

campaign_id = sys.argv[1]

response = delete_campaign(campaign_id)
print(json.dumps(response, indent=4))
