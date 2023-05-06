import voltage
from voltage.ext import commands
import requests
import xml.etree.ElementTree as et

def retrieveServerData():

    url = 'https://online.supertuxkart.net/api/v2/server/get-all'

    try:
        return requests.get(url)
    except Exception as e:
        print(f'Error: {e}')
        sys.exit(1)

    except KeyboardInterrupt:
        print('Interrupt Signal Recieved, quitting...')
        sys.exit(1)

def getServerData():

    data = retrieveServerData()

    if data.status_code == 200:
        with open('servers.xml', 'wb') as f:
            f.write(data.content)
    else:
        return

def setup(client) -> commands.Cog:
    stk = commands.Cog(
        name = 'SuperTuxKart',
        description = 'SuperTuxKart related stuff.'
    )
    
    @stk.command('online', 'See online users.')
    async def stkonline(ctx: commands.CommandContext):

        result = ''

        root = et.parse('/tmp/servers.xml').getroot()

        for _ in root[0]:

                servername = _[0].get('name')
                currtrack = _[0].get('current_track')
                country = _[0].get('country_code')
                maxplayers = _[0].get('max_players')
                currplayers = _[0].get('current_players')
                currai = _[0].get('current_ai')
                players = []

                for player in _[1]:
                    players.append([player.get('country-code'), player.get('username'), int(float(player.get('time-played')))])

                if not players == []:

                    if currtrack == '':
                        result += f'#### [{country}] | {servername} | {currplayers}/{maxplayers}:'
                    else:
                        result += f'#### [{country}] | {servername} | {currplayers}/{maxplayers} | {currtrack}:'

                    result += '\n'

                    for pesant in players:
                        result += (f'##### [{pesant[0]}] {pesant[1]} (Played for {pesant[2]} minutes)\n')

                    if not (int(currplayers) - players.__len__() <= 0):
                        result += (f'###### +{int(currplayers) - players.__len__()}')

                    result += '\n'

        embed = voltage.SendableEmbed(
            title = 'Online right now in STK',
            description = result,
            color = '#f5a9b8'
        )

        await ctx.send(embeds=[embed])

    return stk