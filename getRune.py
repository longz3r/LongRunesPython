import requests
from bs4 import BeautifulSoup
import json

def getRune(championName):
    # Make a GET request to the website
    print("begin GET request")
    requestChampion = championName.replace("'", "")
    response = requests.get(f'https://www.metasrc.com/5v5/champion/{requestChampion.lower().replace(" ", "")}')
    print("GET request end")

    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')


    filteredImage = []
    bigRune = []
    for image in soup.find_all('image'):
        imageUrl = image.get("data-xlink-href")
        if imageUrl.startswith("https://raw.communitydragon.org"):
            filteredImage.append(imageUrl)
        if imageUrl.startswith("https://www.metasrc.com/assets/v"):
            bigRune.append(imageUrl)
    name = []
    name2 = []

    for link in filteredImage:
        tempArray = link.split("/")
        name.append(tempArray[-1][:-4])
    for link in bigRune:
        tempArray = link.split("/")
        name2.append(tempArray[-1][:-4])

    # "Domination": 8100,
    # "Inspiration": 8300,
    # "Precision": 8000,
    # "Resolve": 8400,
    # "Sorcery": 8200,

    with open('ass.json', 'r') as f:
        assRunes = json.load(f)

    print(assRunes[str(name2[4])], assRunes[str(name2[0])],  assRunes[str(name2[5])])
    if name2[0] != name2[5]:
        for i in range(1,100):
            print("Please report this champion name to Long Zer#1086 (discord)")
    if name[5] == "6361":
        name[5] = "nimbuscloak"
    print(name[4:10])
    # print(name[10:13])
    # print(name)

    runes = {
            'current': True,
            'isActive': True,
            'isDeletable': True,
            'isEditable': True,
            'name': f'LongRunes: {championName}',
            'order': 0,
            'primaryStyleId': name2[4],
            'selectedPerkIds': [],
            'subStyleId': name2[0]}

    with open('runes.json', 'r') as f:
        runesQuerry = json.load(f)


    for rune in name[4:10]:
        runes['selectedPerkIds'].append(runesQuerry[rune])
    for rune in name[10:13]:
        runes['selectedPerkIds'].append(runesQuerry[rune])

    return runes

# getRune("K'Sante")