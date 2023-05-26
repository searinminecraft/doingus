import voltage
from voltage.ext import commands

def setup(client) -> commands.Cog:

    tests = commands.Cog(
        name = 'Cog Name',
        description = 'A cog.'
    )

    return tests