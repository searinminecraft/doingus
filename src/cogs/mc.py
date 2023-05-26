import voltage
from voltage.ext import commands
import json
import base64
import aiohttp

api = 'https://api.mcsrvstat.us'

def setup(client) -> commands.Cog:

    mc = commands.Cog(
        name = 'Minecraft',
        description = 'Minecraft related stuff.'
    )

    @mc.command('mcjava-serverstatus', 'Gets information of a Minecraft: Java Edition Server. For Bedrock, please use `mcbedrock-serverstatus`.')
    async def serverstatusjava(ctx: commands.CommandContext, server: str):
        async with aiohttp.ClientSession() as session:
            async with session.get(api + f'/2/{server}') as resp:
                data = await resp.json()

        if data.get('online'):
            embed = voltage.SendableEmbed(
                title = f'Information for server {server}',
                description = f"""**IP**: {data.get('ip')}
**Port**: {data.get('port')}
**Players**: {data.get('players')['online']}/{data.get('players')['max']}
**Online**: {data.get('online')}
**Hostname**: {data.get('hostname')}
**Version**: {data.get('version')}
**Protocol Version**: {data.get('protocol')}""",
                color = '#f5a9b8'
            )
        elif data.get('online') == False and data.get('ip') != '127.0.0.1':
            embed = voltage.SendableEmbed(
                title = f'Information for server {server} (Offline)',
                description = f"""**IP**: {data.get('ip')}
**Port**: {data.get('port')}
**Online**: {data.get('online')}
**Hostname**: {data.get('hostname')}""",
                color = '#f5a9b8'
            )
        else:
            return await ctx.reply('Server does not exist!')

        await ctx.send(embed=embed)

    @mc.command('mcbedrock-serverstatus', 'Gets information of a Minecraft: Bedrock Edition Server. For Java, please use `mcjava-serverstatus`.')
    async def serverstatusjava(ctx: commands.CommandContext, server: str):
        async with aiohttp.ClientSession() as session:
            async with session.get(api + f'/bedrock/2/{server}') as resp:
                data = await resp.json()

        if data.get('online'):
            embed = voltage.SendableEmbed(
                title = f'Information for server {server}',
                description = f"""**IP**: {data.get('ip')}
**Port**: {data.get('port')}
**Players**: {data.get('players')['online']}/{data.get('players')['max']}
**Online**: {data.get('online')}
**Hostname**: {data.get('hostname')}
**Version**: {data.get('version')}
**Protocol Version**: {data.get('protocol')}
**Software**: {data.get('software')}
**Game Mode**: {data.get('gamemode')}
**Server ID**: `{data.get('serverid')}`""",
                color = '#f5a9b8'
            )
        elif data.get('online') == False and data.get('ip') != '127.0.0.1':
            embed = voltage.SendableEmbed(
                title = f'Information for server {server} (Offline)',
                description = f"""**IP**: {data.get('ip')}
**Port**: {data.get('port')}
**Online**: {data.get('online')}
**Hostname**: {data.get('hostname')}""",
                color = '#f5a9b8'
            )
        else:
            return await ctx.reply('Server does not exist!')

        await ctx.send(embed=embed)


    return mc

