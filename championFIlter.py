import requests
import json

# Make a GET request to the JSON API
response = requests.get('https://ddragon.leagueoflegends.com/cdn/13.5.1/data/en_US/champion.json')

# Parse the response as JSON
data = json.loads(response.text)

# Define a function to filter the data
def filter_data(data):
    filtered_data = {}
    for key, value in data['data'].items():
        filtered_champion = {
            "key": value["key"],
            "name": value["name"]
        }
        filtered_data[value["key"]] = filtered_champion["name"]
    return filtered_data

# Call the filter_data function and write the result to a file
filtered_data = filter_data(data)
with open('filtered_champion.json', 'w') as f:
    json.dump(filtered_data, f, indent=2)
