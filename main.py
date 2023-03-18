from lcu_driver import Connector
import time

connector = Connector()
from querryChampion import querryChampion
from createPage import createPage

# fired when LCU API is ready to be used
@connector.ready
async def connect(connection):
    print('LCU API is ready to be used.')
    data = await connection.request('get', '/lol-summoner/v1/current-summoner')
    if data.status != 200: 
        print("Cannot access to LeagueAPI")
    else:
        resp = await data.json()
        print(f"Welcome", resp["displayName"])

    temp = {}
    while True:
        smt = await connection.request('get', '/lol-champ-select/v1/current-champion')
        smt = await smt.json()
        if smt == temp:
            temp = smt
            pass
        else:
            temp = smt
            if smt == {'errorCode': 'RPC_ERROR', 'httpStatus': 404, 'implementationDetails': {}, 'message': 'No active delegate'}:
                pass
            elif smt == 0:
                pass
            else:
                print("Querrying rune for", querryChampion(smt))
                await createPage(connection, querryChampion(smt))

        time.sleep(1)


@connector.ws.register('/lol-summoner/v1/current-champion', event_types=('UPDATE',))
async def icon_changed(connection, event):
    print(event)

@connector.close
async def disconnect(_):
    print('The client have been closed!')


connector.start()