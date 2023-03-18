import json

# Load the filtered data from the JSON file into a dictionary
with open('filtered_champion.json', 'r') as f:
    filtered_data = json.load(f)

def querryChampion(id):
    return filtered_data[str(id)]