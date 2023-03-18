async def createPage(connection, championName):
    pages = await connection.request('get', "/lol-perks/v1/pages")
    pages = await pages.json()

    data={'autoModifiedSelections': [],
            'current': True,
            'isActive': True,
            'isDeletable': True,
            'isEditable': True,
            'name': 'Page adasdadsad',
            'order': 0,
            'primaryStyleId': 8100,
            'selectedPerkIds': [8124, 8143, 8120, 8134, 9105, 8299, 5005, 5002, 5001],
            'subStyleId': 8000}
    

    if len(pages) == 0:
        #create page function
        print("Create page")
        await connection.request("post", "/lol-perks/v1/pages/", data=data)
    else:
        #update page
        currentPerk = await connection.request('get', "/lol-perks/v1/currentpage")
        currentPerk = await currentPerk.json()

        await connection.request("put", "/lol-perks/v1/pages/" + str(currentPerk["id"]), data=data)