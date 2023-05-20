import voltage
from voltage.ext import commands
import requests
import xml.etree.ElementTree as et
import subprocess
from dotenv import load_dotenv, dotenv_values

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
        return data.text
    else:
        return

# Thanks DernisNW for giving the code for converting big ip addresses to readable ones.
def bigip(x):
    return '.'.join([str(y) for y in int.to_bytes(int(x), 4, 'big')])


def setup(client) -> commands.Cog:
    stk = commands.Cog(
        name = 'SuperTuxKart',
        description = 'SuperTuxKart related stuff.'
    )
    
    @stk.command('online', 'See online users.')
    async def stkonline(ctx: commands.CommandContext):

        result = ''

        data = getServerData()
        root = et.fromstring(data.replace('\n', ''))

        for _ in root[0]:

                servername = _[0].get('name')
                currtrack = _[0].get('current_track')
                country = _[0].get('country_code')
                maxplayers = _[0].get('max_players')
                currplayers = _[0].get('current_players')
                password: int = int(_[0].get('password'))
                ip: int = int(_[0].get('ip'))
                id: int = int(_[0].get('id'))
                port: int = int(_[0].get('port'))
                players = []

                formattedip = bigip(ip)

                for player in _[1]:
                    players.append([player.get('country-code'), player.get('username'), int(float(player.get('time-played')))])

                if not players == []:

                    result += f'**{"".join(chr(127397 + ord(k)) for k in country)} {servername} ({formattedip}:{port})**\n'
                    result += f'**Server ID**: {id}\n'
                    result += f'**Current Track**: {currtrack}\n'
                    result += f'**Password Protected**: {"Yes" if password == 1 else "No"}\n'
                    result += f'**Players: ({currplayers}/{maxplayers})**\n'
                    result += '```\n'

                    for pesant in players:
                        result += (f'{"".join(chr(127397 + ord(k)) for k in pesant[0])} {pesant[1]} (Played for {pesant[2]} minutes)\n')

                    if not (int(currplayers) - players.__len__() <= 0):
                        result += (f'+{int(currplayers) - players.__len__()}\n')
                    
                    result += '```\n'

                    result += '\n'
            
        embed = voltage.SendableEmbed(
            title = 'Online right now in STK',
            description = (result if result != '' else 'Uh, it appears that nobody is online... Have this instead: OwO'),
            color = '#f5a9b8'
        )

        await ctx.send(embeds=[embed])

    @stk.command('stk-serversearch', 'Search for a server')
    async def serversearch(ctx: commands.CommandContext, *, query: str):
        root = et.fromstring(getServerData())
        results = []
        output = ''

        for _ in root[0]:

            if _[0].get('name').lower().find(query.lower()) >= 0:
                results.append(_[0].attrib)

        for result in results:
            servername = result.get('name')
            currtrack = result.get('current_track')
            country = result.get('country_code')
            maxplayers = result.get('max_players')
            currplayers = result.get('current_players')
            password: int = int(result.get('password'))
            ip: int = int(result.get('ip'))
            id: int = int(result.get('id'))
            port: int = int(result.get('port'))

            output += f'**{"".join(chr(127397 + ord(k)) for k in country)} {servername} ({bigip(ip)}:{port})**\n'
            output += f'**Server ID**: {id}\n'
            output += f'**Current Track**: {currtrack}\n'
            output += f'**Password Protected**: {"Yes" if password == 1 else "No"}\n'
            output += f'**Players**: {currplayers}/{maxplayers}\n'
            output += '\n'

        if len(output) > 2000:
            return await ctx.send("Too many results.")

        embed = voltage.SendableEmbed(
            title = f'Search Results ({results.__len__()})',
            description = output if output != '' else 'No results :(',
            color = '#f5a9b8'
        )

        await ctx.send(embed=embed)

    @stk.command('top-ranked', 'See top ranked players.')
    async def topranked(ctx: commands.CommandContext):
        load_dotenv()
        data = subprocess.run(['curl', '-sX', 'POST', '-d', f'userid={dotenv_values()["stk_userid"]}&token={dotenv_values()["stk_token"]}', 'https://online.supertuxkart.net/api/v2/user/top-players'], stdout=subprocess.PIPE).stdout.decode('utf-8')
        root = et.fromstring(data)
        output = ''
        place = 1

        for player in root[0].findall('player'):
            output += f'{place}. **{player.get("username")}**: {player.get("scores")}\n'
            place += 1

        embed = voltage.SendableEmbed(
            title = 'Top 10 ranked players',
            description = output,
            color = '#f5a9b8'
        )

        await ctx.send(embed=embed)

    @stk.command('stk-usersearch', 'Search for a user.')
    async def usersearch(ctx: commands.CommandContext, *, query: str):
        load_dotenv()
        data = subprocess.run(['curl', '-sX', 'POST', '-d', f'userid={dotenv_values()["stk_userid"]}&token={dotenv_values()["stk_token"]}&search-string={query.lower()}', 'https://online.supertuxkart.net/api/v2/user/user-search'], stdout=subprocess.PIPE).stdout.decode('utf-8')
        root = et.fromstring(data)
        output = ''

        for _ in root[0].findall('user'):
            output += f'* {_.get("user_name")} ({_.get("id")})\n'

        if len(output) > 2000:
            return await ctx.send('I couldn\'t fit all of it due to character limit.')

        embed = voltage.SendableEmbed(
            title = f'Search results for "{query}"',
            description = output if output != '' else 'No results :(',
            color = '#f5a9b8'
        )

        await ctx.send(embed=embed)

    @stk.command('stkaccount', 'Know what STK account is being used!', ['stk-whoami'])
    async def whoami(ctx: commands.CommandContext):
        load_dotenv()

        embed = voltage.SendableEmbed(
            title = 'Who am I?',
            description = f'Hi! I\'m {dotenv_values()["stk_username"]}! My User ID is {dotenv_values()["stk_userid"]}. OwO',
            color = '#f5a9b8'
        )

        await ctx.send(embed=embed)

       
    return stk
