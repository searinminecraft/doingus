import voltage
from voltage.ext import commands

def setup(client) -> commands.Cog:

    cogname = commands.Cog(
        name = 'Cog Name',
        description = 'A cog.'
    )

    @cogname.command(name = 'command', description = 'amogus')
    async def commandname(ctx: commands.CommandContext):
        # do stuff

        await ctx.send('amogus')

    return cogname