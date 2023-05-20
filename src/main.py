import voltage
from dotenv import load_dotenv, dotenv_values, set_key
from voltage.ext import commands
import random
import asyncio
import aiohttp
import subprocess
import xml.etree.ElementTree as et

load_dotenv()
REVOLT_TOKEN = dotenv_values()['revolt_token']
STK_USERNAME = None
STK_PASSWORD = None

try:
    STK_USERNAME = dotenv_values()['stk_username']
    STK_PASSWORD = dotenv_values()['stk_password']
except KeyError as k:
    print(f'{k} was not provided. Disabling SuperTuxKart features.')

class MyHelpCommand(commands.HelpCommand):
    async def send_help(self, ctx: commands.CommandContext):
        embed = voltage.SendableEmbed(
            title="Help",
            description=f"Use `{ctx.prefix}help <command>` to get help for a command.",
            colour="#f5a9b8",
            icon_url=ctx.author.display_avatar.url
        )
        text = "\n### **No Category**\n"
        for command in self.client.commands.values():
            if command.cog is None:
                text += f"> {command.name}\n"
        for i in self.client.cogs.values():
            text += f"\n### **{i.name}**\n{i.description}\n"
            for j in i.commands:
                text += f"\n> {j.name}"
        if embed.description:
            embed.description += text
        return await ctx.reply(f"[]({ctx.author.id})", embed=embed)

client = commands.CommandsClient('-', help_command=MyHelpCommand)

@client.error('message')
async def on_error(error:Exception, message:voltage.Message):
    if isinstance(error, voltage.CommandNotFound):
        embed = voltage.SendableEmbed(
            title = 'Well, that was unexpected...',
            description = 'That command doesn\'t exist you little dingus',
            color = '#f5a9b8' 
        )

        return await message.reply(embeds=[embed])

    if isinstance(error, voltage.NotBotOwner):
        embed = voltage.SendableEmbed(
            title = 'Bro?',
            description = 'You\'re not my bot owner, sussy baka.',
            color = '#f5a9b8'
        )

        return await message.reply(embeds='embed')
    
    if isinstance(error, voltage.MemberNotFound):
        embed = voltage.SendableEmbed(
            title = 'AAAAAAAAAAAAAA',
            description = 'Couldn\'t find user.',
            color = '#f5a9b8'
        )
        
        return await message.reply(embeds=[embed])
   
    embed = voltage.SendableEmbed(
        title = 'I\'m sorry, but an error occured!',
        description = f'```\n{error}\n```',
        color = '#f5a9b8'
    )

    await message.reply(embeds=[embed])
    
async def status():
	for i in range(1, 2147483647):
		statuses = [
			'OwO',
			'Revolt >>>>>>>',
			f'Making {len(client.members)} members smile',
			'kimden is sweet',
			'Watching you!',
			'-help | https://github.com/searinminecraft/doingus',
			f'Random number: {random.randint(1, 10000)}',
			'I love you, and everyone!',
			'aeasus',
            'Simple, fast, systemd-free!',
            'See online STK users with -online!',
            f'Python Powered! Voltage {voltage.__version__}'
		]
		
		status = random.choice(statuses)
		await client.set_status(status, voltage.PresenceType.online)
		await asyncio.sleep(10)

async def stkAuth():
    print(f'Authenticating SuperTuxKart Account {STK_USERNAME}...')
    data = subprocess.run(['curl', '-sX', 'POST', '-d', f'username={STK_USERNAME}&password={STK_PASSWORD}&save_session=true', 'https://online.supertuxkart.net/api/v2/user/connect'], stdout=subprocess.PIPE).stdout.decode('utf-8')
    root = et.fromstring(data)
    print(root.attrib)
    token = root.get('token')
    userid = root.get('userid')
    
    if token is None:
        print(f'Failed to authenticate: {root.get("info")}')
        return

    set_key('.env', "stk_token", token)
    set_key('.env', "stk_userid", userid)

    load_dotenv()

    print(f"""
Successfully logged in as {STK_USERNAME}@stk!

UserID: {userid}
Token: {token}
""")

async def loop():
    for i in range(1, 2147483647):
        statuses = [
            'OwO',
			'Revolt >>>>>>>',
			f'Making {len(client.members)} members smile',
			'kimden is sweet',
			'Watching you!',
			'-help | https://github.com/searinminecraft/doingus',
			f'Random number: {random.randint(1, 10000)}',
			'I love you, and everyone!',
			'aeasus',
            'Simple, fast, systemd-free!',
            'See online STK users with -online!',
            f'Python Powered! Voltage {voltage.__version__}'
		]
		
        status = random.choice(statuses)
        print(f'Setting current status to {status}')
        await client.set_status(status, voltage.PresenceType.online)

        if STK_PASSWORD is not None and STK_USERNAME is not None:
            print(f'Polling STK Account..')
            data = subprocess.run(['curl', '-sX', 'POST', '-d', f'userid={dotenv_values()["stk_userid"]}&token={dotenv_values()["stk_token"]}', 'https://online.supertuxkart.net/api/v2/user/poll'], stdout=subprocess.PIPE).stdout.decode('utf-8')
            root = et.fromstring(data)

            if root.get('success') == 'no':
                print(f'Poll request failed: {root.get("info")}. Attempting to reauthenticate.')
                await stkAuth()

        await asyncio.sleep(120)

@client.listen('ready')
async def on_ready():
    if STK_PASSWORD is not None and STK_USERNAME is not None:
        print('Start authenticating stk')
        await stkAuth()

    print('Start loop')
    await loop()

print('Loading Cogs...')
client.add_extension('cogs.fun')
client.add_extension('cogs.misc')
if STK_PASSWORD is not None and STK_USERNAME is not None:
    client.add_extension('cogs.stk')
client.add_extension('cogs.mc')
client.add_extension('cogs.text')
client.add_extension('cogs.image')
client.add_extension('cogs.utility')
client.add_extension('cogs.games')
print('Successfully Loaded Cogs.')

@commands.is_owner()
@client.command('loadcog', 'Loads a cog.')
async def loadcog(ctx: commands.CommandContext, cog: str = None):
    if cog is None:
        return await ctx.reply('Please, specify a cog!')
    
    client.add_extension(f'cogs.{cog}')
    await ctx.reply(f'Successfully loaded cog {cog}')

@commands.is_owner()
@client.command('unloadcog', 'Unloads a cog.')
async def unloadcog(ctx: commands.CommandContext, cog: str = None):
    if cog is None:
        return await ctx.reply('Please, specify a cog!')
    
    client.remove_extension(f'cogs.{cog}')
    await ctx.reply(f'Successfully unloaded cog {cog}')

@commands.is_owner()
@client.command('reloadcog', 'Loads a cog.')
async def reloadcog(ctx: commands.CommandContext, cog: str = None):
    if cog is None:
        return await ctx.reply('Please, specify a cog!')
    
    client.reload_extension(f'cogs.{cog}')
    await ctx.reply(f'Successfully reloaded cog {cog}')

client.run(REVOLT_TOKEN)
