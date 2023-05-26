import voltage
import math
from voltage.ext import commands
import random
import asyncio

class TickTackToeGame:
    """A simple class which represents and handles a game of tick tack toe"""
    def __init__(self, player1: voltage.Member, player2: voltage.Member):
        self.player = player1
        self.players = [player1, player2]
        self.board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        self.turn = 0
        self.winner = None
        self.draw = False

    def render_board(self):
        """Renders the board as a string"""
        board = str()
        symbols = ["$\\textcolor{red}{\\textsf{X}}$", "$\\textcolor{yellow}{\\textsf{O}}$"]
        for i, row in enumerate(self.board):
            board += "|"
            if i == 1:
                board += "---|---|---|\n"
            for j, cell in enumerate(row):
                if cell == 1:
                    symbol = symbols[0]
                elif cell == -1:
                    symbol = symbols[1]
                else:
                    symbol = str(i*3+j+1)
                board += f" {symbol} |"
            board += "\n"
        return board

    def check_winner(self):
        player = self.players[(self.turn+1)%2]
        for i in self.board:
            if i[0] == i[1] == i[2] != 0:
                self.winner = player
                return True
        for i in range(3):
            if self.board[0][i] == self.board[1][i] == self.board[2][i] != 0:
                self.winner = player
                return True
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != 0:
            self.winner = player
            return True
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != 0:
            self.winner = player
            return True
        if 0 not in self.board[0] and 0 not in self.board[1] and 0 not in self.board[2]:
            self.draw = True
            return True
        return False

    def make_move(self, place: int):
        """Makes a move on the board"""
        x, y = math.ceil(place/3), (place-1)%3
        x -= 1
        self.board[x][y] = 1 if self.turn%2 == 0 else -1
        self.turn += 1
        self.player = self.players[self.turn%2]

    def __str__(self):
        return f"{self.player.mention}'s turn\n{self.render_board()}"

    @property
    def available(self):
        """Returns a list of available moves"""
        available = []
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == 0:
                    available.append(i*3+j+1)
        return available

    @property
    def is_over(self):
        """Returns whether the game is over"""
        self.check_winner()
        return self.winner is not None or self.draw


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
        
    @games.command('tictactoe', 'Face someone in the ultimate game of skill, Tic-Tac-Toe.')
    async def ttt(ctx: commands.CommandContext, member: voltage.Member = None):
        if member is None:
            return await ctx.reply('Please specify a user you want to challenge.')
        msg = await ctx.send(f"{ctx.author.display_name} challenged {member.display_name} to an epic game of Tic-Tac-Toe")
        game = TickTackToeGame(ctx.author, member)
        while not game.is_over:
            await asyncio.sleep(1)
            await msg.edit(game)
            try:
                place = int((await client.wait_for("message", timeout=60, check=lambda m: m.author == game.player and m.channel == ctx.channel and m.content in ''.join([str(i) for i in game.available]))).content)
            except asyncio.TimeoutError:
                await ctx.send(f"{game.player.display_name} forfeited!")
                game.winner = game.players[(game.turn+1)%2]
                break
            game.make_move(place)
        await msg.edit(game)
        if game.draw:
            await ctx.send(f"{ctx.author.display_name} and {member.display_name} tied!")
        elif game.winner:
            await ctx.send(f"{game.winner.mention} won!")
        else:
            await ctx.send("..huh")    
    return games
