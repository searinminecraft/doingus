import voltage
from voltage.ext import commands
import random

def setup(client) -> commands.Cog:
    
    games = commands.Cog(
        'Games',
        'Some simple games. I\'m bad at python so most of them are simple.'
    )

    @games.command(name='rps', description='Play a game of (totally fair) rock paper scissors.')
    async def rps(ctx: commands.CommandContext, choice = None):
        if choice is None:
            await ctx.reply('Specify if you want to go for rock, paper, or scissors!')
            return

        choices = ['rock', 'paper', 'scissors']

        if not choices.__contains__(choice):
            await ctx.reply('Invalid choice! It must be either rock, paper or scissors!!1')
            return

        state = ''
        result = random.choice(choices)

        if (result == 'rock' and choice == 'scissors') or (result == 'scissors' and choice == 'paper') or (result == 'paper' and choice == 'rock'):
            state = 'You Lose!'
        elif result == choice:
            state = 'It\'s a draw!'
        else:
            state = 'You Win!'

        embed = voltage.SendableEmbed(
            title = 'Rock Paper Scissors',
            description = f'You went for: {choice}\nThe bot went for: {result}\n\n{state}'
        )

        await ctx.send(embeds=[embed])

    return games