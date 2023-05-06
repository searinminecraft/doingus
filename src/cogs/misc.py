import voltage
from voltage.ext import commands
import subprocess
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
            title = 'Doingus',
            description = f'Doingus is powered by Voltage. Version {voltage.__version__}',
            color = '#f5a9b8'
        )

        await ctx.reply(embeds=[embed])

    @misc.command()
    async def echo(ctx: commands.CommandContext, msg: str='UwU'):
        """Make doingus send a message of your liking."""
        
        if ctx.author.bot:
            await ctx.reply('Sorry, only real Revolt users can do this. Nice try!')
            return

        await ctx.send(msg)
    
    @misc.command('neofetch', 'Outputs the neofetch of where the bot is running.', ['btw'])
    async def neofetch(ctx: commands.CommandContext):
        output = subprocess.run(['neofetch', '--stdout'], stdout=subprocess.PIPE).stdout.decode('utf-8')

        embed = voltage.SendableEmbed(
            title = 'neofetch',
            description = f'```\n{output}\n```',
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
    
    return misc