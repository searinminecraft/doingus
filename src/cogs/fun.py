import voltage
from voltage.ext import commands
import random
import asyncio
import subprocess
import math

def setup(client) -> commands.Cog:
    fun = commands.Cog(
        "Fun",
        "Some fun little commands."
    )

    @fun.command('coinflip', 'Flip a coin.')
    async def coinflip(ctx: commands.CommandContext):
        
        choice = random.choice(['heads','tails'])

        await ctx.reply(f'You got {choice}!')

    @fun.command('amogus', 'Sends a very sussy message.', ['sus', 'sussy', 'sussybaka'])
    async def amogus(ctx: commands.CommandContext):

        await ctx.reply("SUS AMONGUS \n# :01GSZ43ACQE6DHNB0KTDKTF6JP: :01GSZ43ACQE6DHNB0KTDKTF6JP: :01GSZ43ACQE6DHNB0KTDKTF6JP: :01GSZ43ACQE6DHNB0KTDKTF6JP: :01GSZ43ACQE6DHNB0KTDKTF6JP: :01GSZ43ACQE6DHNB0KTDKTF6JP:")

    @fun.command('hack', 'Hack someone!', ['hax'])
    async def hack(ctx: commands.CommandContext, user: voltage.Member = None):
        
        if user is None:
            await ctx.reply('Specify a person you want to hack!')
            return
        try:
            msg = await ctx.send(f'Starting to hack **{user.name}**...')
            await asyncio.sleep(3)
            await msg.edit(f'Attempting to gain root access...')
            await asyncio.sleep(5)
            await msg.edit('Got root access! Getting sensitive information...')
            await asyncio.sleep(3)
            await msg.edit('Analyzing for illegal stuff...')
            await asyncio.sleep(5)
            await msg.edit(f'Reporting **{user.name}** to contact@revolt.chat for violating the AUP...')
            await asyncio.sleep(2)
            await msg.edit(f'Destroying **{user.name}**\'s computer using `rm -rf / --no-preserve-root`...')
            await asyncio.sleep(6)
            await msg.edit(f'Done hacking **{user.name}**!')

            await msg.reply('The _totally real_ and dangerous hack is complete.')
        except:
            await ctx.send(f'ok the hacking stopped because someone deleted my message while i was hacking **{user.name}**. rude.')

    @fun.command('8ball', 'Ask the Magic 8 Ball!')
    async def eightball(ctx: commands.CommandContext, *, question):
        
        print(question)

        if question is None:
            await ctx.reply('Please ask a question!')
            return
        
        result = random.choice(
            [
                'It is certain.',
                'It is decidedly so.',
                'Without a doubt.',
                'Yes definitely.',
                'You may rely on it.',
                'As I see it, yes.',
                'Most likely.',
                'Outlook good.',
                'Yes.',
                'Signs point to yes.',
                'Reply hazy, try again.',
                'Ask again later.',
                'Better not tell you now.',
                'Cannot predict now.',
                'Concentrate and ask again.',
                'Don\'t count on it.',
                'My reply is no.',
                'My sources say no.',
                'Outlook not so good.',
                'Very doubtful.'
            ]
        )

        embed = voltage.SendableEmbed(
            title = question,
            description = result,
            color = '#f5a9b8'
        )

        await ctx.send(embeds=[embed])
       
    @fun.command('blank', 'creates a blank message :trol:')
    async def blankmessage(ctx: commands.CommandContext):
        await ctx.send('\n')

    @fun.command('susrate', 'how sus are u? :amogus:')
    async def susrate(ctx: commands.CommandContext, member: voltage.Member = None):
        if member is None:
            member = ctx.author
        
        await ctx.reply(f"{member.display_name} is **{random.randint(0, 100)}%** sus :amogus:")

    @fun.command('impersonate', 'impersonate someone!')
    async def impersonate(ctx: commands.CommandContext, member: voltage.Member, *, message = 'UwU'):

        rc = None

        for role in member.roles:
            if role.color is not None:
                rc = role.color
                break

            rc = '#ffffff'

        await ctx.send(message, masquerade=voltage.MessageMasquerade(member.name, member.avatar.url, color=rc))

    return fun
