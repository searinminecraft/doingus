import voltage
from dotenv import load_dotenv, dotenv_values
from voltage.ext import commands

load_dotenv()
REVOLT_TOKEN = dotenv_values()['revolt_token']

client = commands.CommandsClient('-')


@client.error('message')
async def on_error(error:Exception, message:voltage.Message):
    if isinstance(error, voltage.CommandNotFound):
        return

    await message.reply(f'I\'m sorry, but an error occured! Heres the error:\n\n```\n{error}\n```')

client.add_extension('cogs.fun')
client.add_extension('cogs.misc')
client.add_extension('cogs.utility')
client.add_extension('cogs.games')

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
