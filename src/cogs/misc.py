import voltage
from voltage.ext import commands
import subprocess
import random
import asyncio
import time

def setup(client) -> commands.Cog:
    misc = commands.Cog(
        'Miscellaneous',
        'Random stuff :yed:'
    )

    @misc.command()
    async def test(ctx: commands.CommandContext):
        embed = voltage.SendableEmbed(
            title='embed title',
            description='embed description',
            color='#f5a9b8',
            icon_url='https://static.wikia.nocookie.net/amogus/images/c/cb/Susremaster.png/revision/latest'
        )

        await ctx.reply('Beep Boop.', embeds=[embed])

    @misc.command()
    async def version(ctx: commands.CommandContext):
        """Version reporter"""
        embed = voltage.SendableEmbed(
            title = client.user.name,
            description = f'{client.user.name} is powered by Voltage. Version {voltage.__version__}',
            color = '#f5a9b8',
            icon_url = client.user.avatar.url if client.user.avatar else client.user.default_avatar.url
        )

        await ctx.reply(embeds=[embed])

    @misc.command()
    async def echo(ctx: commands.CommandContext, *, msg: str='UwU'):
        """Make doingus send a message of your liking."""
        
        #if ctx.author.bot:
        #    await ctx.reply('Sorry, only real Revolt users can do this. Nice try!')
        #    return

        await ctx.send(msg)

    @misc.command('embedecho', 'Same as `echo`, but sends it in an embed.')
    async def embedecho(ctx: commands.CommandContext, *, msg: str = 'UwU'):
        await ctx.send(embed=voltage.SendableEmbed(
            description = msg,
            color = '#f5a9b8'
        ))
    
    @misc.command('neofetch', 'Outputs the neofetch of where the bot is running.', ['btw'])
    async def neofetch(ctx: commands.CommandContext):
        output = subprocess.run(['neofetch', '--stdout'], stdout=subprocess.PIPE).stdout.decode('utf-8')

        embed = voltage.SendableEmbed(
            title = 'neofetch',
            description = f"""```
{output}
```""",
            color = '#f5a9b8'
        )

        await ctx.send(embeds=[embed])

    @misc.command('ping', 'Get ping', ['lag', 'latency'])
    async def ping(ctx: commands.CommandContext):
        before = time.time()
        msg = await ctx.send('Measuring ping...')
        after = time.time()

        await msg.edit(f'Pong! {int((after - before) * 1000)}ms')

    @misc.command('sourcecode')
    async def sourcecode(ctx: commands.CommandContext):
        await ctx.reply('i am not supposed to give a source code to you, sussy baka')
        await asyncio.sleep(4)
        await ctx.reply('anyways, here u go: https://github.com/searinminecraft/doingus')


    @misc.command()
    async def chrash(ctx: commands.CommandContext):
        embed = voltage.SendableEmbed(
            title = 'aaaaaaaaaa',
            description = 'bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb',
            color = '#f5a9b8'
        )

        await ctx.send(embeds=[embed])
    

    return misc
