import json
import sys

from api import status_campaign


if len(sys.argv) != 2:
    print(f"Usage: python {sys.argv[0]} <campaign_id>")
    exit()

campaign_id = sys.argv[1]

response = status_campaign(campaign_id)
print(json.dumps(response, indent=4))
