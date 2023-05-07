import voltage
from voltage.ext import commands
import random
import asyncio
import subprocess

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

    @fun.command('stallman', 'Sends the GNU/Linux interjection copypasta. You can replace \'Linux\' with any word you want.', ['interject'])
    async def stallman(ctx: commands.CommandContext, linux: str = 'Linux'):

        interjection: str = "I'd just like to interject for a moment. What you're referring to as Linux, is in fact, GNU/Linux, or as I've recently taken to calling it, GNU plus Linux. Linux is not an operating system unto itself, but rather another free component of a fully functioning GNU system made useful by the GNU corelibs, shell utilities and vital system components comprising a full OS as defined by POSIX.\n\nMany computer users run a modified version of the GNU system every day, without realizing it. Through a peculiar turn of events, the version of GNU which is widely used today is often called \"Linux\", and many of its users are not aware that it is basically the GNU system, developed by the GNU Project.\n\nThere really is a Linux, and these people are using it, but it is just a part of the system they use. Linux is the kernel: the program in the system that allocates the machine's resources to the other programs that you run. The kernel is an essential part of an operating system, but useless by itself; it can only function in the context of a complete operating system. Linux is normally used in combination with the GNU operating system: the whole system is basically GNU with Linux added, or GNU/Linux. All the so-called \"Linux\" distributions are really distributions of GNU/Linux."

        await ctx.reply(interjection.replace("Linux", linux))

    @fun.command('hack', 'Hack someone!', ['hax'])
    async def hack(ctx: commands.CommandContext, user: voltage.Member = None):
        
        if user is None:
            await ctx.reply('Specify a person you want to hack!')
            return
        
        msg = await ctx.send(f'Starting to hack {user.name}...')
        await asyncio.sleep(3)
        await msg.edit(f'Attempting to gain root access...')
        await asyncio.sleep(5)
        await msg.edit('Got root access! Getting sensitive information...')
        await asyncio.sleep(3)
        await msg.edit('Analyzing for illegal stuff...')
        await asyncio.sleep(5)
        await msg.edit(f'Reporting {user.name} to contact@revolt.chat for violating the AUP...')
        await asyncio.sleep(2)
        await msg.edit(f'Destroying {user.name}\'s computer using `rm -rf / --no-preserve-root`...')
        await asyncio.sleep(6)
        await msg.edit(f'Done hacking {user.name}!')

        await msg.reply('The _totally real_ and dangerous hack is complete.')

    @fun.command('8ball', 'Ask the Magic 8 Ball!')
    async def eightball(ctx: commands.CommandContext, question: str = None):
        
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

    @fun.command('eavesdrop', 'Someone could be doing something nasty!')
    async def eavesdrop(ctx: commands.CommandContext):
        random = subprocess.run(['sh', '-c', 'base64 /dev/urandom | head -c 25'], stdout=subprocess.PIPE).stdout.decode('utf-8')

        msg = f"```\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n@    WARNING: REMOTE HOST IDENTIFICATION HAS CHANGED!     @\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\nIT IS POSSIBLE THAT SOMEONE IS DOING SOMETHING NASTY!\nSomeone could be eavesdropping on you right now (man-in-the-middle attack)!\nIt is also possible that a host key has just been changed.\nThe fingerprint for the ED25519 key sent by the remote host is\nSHA256:{random}.\nPlease contact your system administrator.\nAdd correct host key in /home/doingus/.ssh/known_hosts to get rid of this message.\nOffending ED25519 key in /home/doingus/.ssh/known_hosts:69420\nHost key for 127.0.0.1 has changed and you have requested strict checking.\nHost key verification failed.\n```"

        await ctx.send(msg)
    return fun
