import requests
import json

# Make a GET request to the JSON API
response = requests.get('https://ddragon.leagueoflegends.com/cdn/13.5.1/data/en_US/runesReforged.json')

# Parse the response as JSON
data = json.loads(response.text)
# Define a function to filter the data
def filter_data(data):
    filtered_data = {
        "statmodsattackspeedicon": 5005,
        "statmodsadaptiveforceicon": 5008,
        "statmodsarmoricon": 5002,
        "statmodsmagicresicon.magicresist_fix": 5003,
        "statmodshealthscalingicon": 5001,
        "statmodscdrscalingicon": 5007,
    }
    for item in data:
        filtered_data[item["key"]] = item["id"]
        for slot in item["slots"]:
            for rune in slot["runes"]:
                if rune['key'].lower() == "lethaltempo":
                    rune['key'] = "lethaltempotemp"
                if rune['key'].lower() == "tasteofblood":
                    rune['key'] = "greenterror_tasteofblood"
                filtered_data[rune['key'].lower()] = rune['id']
    return filtered_data


# Call the filter_data function and write the result to a file
filtered_data = filter_data(data)
with open('runes.json', 'w') as f:
    json.dump(filtered_data, f, indent=2)
