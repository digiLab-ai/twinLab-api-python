import json

from api import list_campaigns


response = list_campaigns()
print(json.dumps(response, indent=4))
