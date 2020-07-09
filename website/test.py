

import json
import requests

headers = {
    "hibp-api-key": "38eb580ec92d4403becca47370ac9d1f"
}

response = requests.get('https://haveibeenpwned.com/api/v3/breachedaccount/natsuki951@hotmail.com?truncateResponse=false', headers=headers)

breachdata = response.json()

# print(response)
cleansedbreach = []
for compromised in breachdata:
    cleansedbreach.append(
        {
            'Name':compromised['Name'],
            'BreachDate':compromised['BreachDate'],
            'LogoPath':compromised['LogoPath'],
            'Description':compromised['Description']
        }
    )

print(cleansedbreach)
# print(json.dumps(cleansedbreach, indent=4, sort_keys=True))



