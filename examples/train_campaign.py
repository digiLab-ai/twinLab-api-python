import json
import sys

from api import train_campaign


if len(sys.argv) != 4:
    print(
        f"Usage: python {sys.argv[0]} <path/to/parameters.json> <campaign_id> <processor>")
    exit()

filepath = sys.argv[1]
campaign_id = sys.argv[2]
processor = sys.argv[3]

response = train_campaign(filepath, campaign_id, processor)
print(json.dumps(response, indent=4))
