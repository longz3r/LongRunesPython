from getRune import getRune

async def createPage(connection, championName):
    pages = await connection.request('get', "/lol-perks/v1/pages")
    pages = await pages.json()

    data=getRune(championName)
    print(data)
    

    if len(pages) == 0:
        #create page function
        print("Create page")
        await connection.request("post", "/lol-perks/v1/pages/", data=data)
    else:
        #update page
        currentPerk = await connection.request('get', "/lol-perks/v1/currentpage")
        currentPerk = await currentPerk.json()

        await connection.request("put", "/lol-perks/v1/pages/" + str(currentPerk["id"]), data=data)