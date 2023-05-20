import voltage
from voltage.ext import commands
import random

def setup(client) -> commands.Cog:
    text = commands.Cog(
        name = 'Text',
        description = 'Text manipulation and other stuff.'
    )

    @text.command('owoify', 'Makes a message you reply to OwO', ['owo'])
    async def owoify(ctx: commands.CommandContext):
        
        try:
            if ctx.message.replies[0] is None:
                return await ctx.reply('The message you replied to has no message content in it.')

            await ctx.send(str(
            ctx.message.replies[0].content)
                .replace('r', 'w')
                .replace('R', 'W')
                .replace('o', 'u')
                .replace('O', 'U')
                .replace('l', 'w')
                .replace('L', 'W')
            )
            
        except Exception:
            return await ctx.reply('Please reply to a message you want to owoify.')

    @text.command('why')
    async def why(ctx: commands.CommandContext):
        result = random.choice([
            'Because the only way to fix your windows pc is rebooting.',
            'because https://online.supertuxkart.net/api sucks',
            'because searinminecraft is always accused of owning alt accounts from the philippines',
            'because hollyleaf keeps beating me',
            'because revolt is the best',
            'because `sudo rm -rf / --no-preserve-root` solves everything',
            'because `Session not valid. Please sign in`',
            'because `no module found \'requests\'`',
            'because nobody asked.',
            'because aeasus',
            'because supertuxkart authentication sucks',
            'because i love insert, the creator of revolt',
            'because i dont care about your opinion',
            'because bluetooth tethering',
            'because creating a stk server from stk leaks ur ip',
            'because poland ranked is more like poland lagged',
            'because kimden is sweet',
            'because i love pineapple pizza',
            'because searinminecraft drew my avatar',
            'because None',
            'because because because',
            'because i use arch btw',
            'because someone typed https://revolt.cat instead of revolt.chat',
            'because kernel panic - not syncing: attempted to kill init! (exitcode=0x00000000)',
            'because i know youre spamming this command',
            'because automod'
        ])

        await ctx.send(result)

    @text.command('eavesdrop', 'Someone could be eavesdropping on you right now!')
    async def eavesdrop(ctx: commands.CommandContext):
        randomstring = subprocess.run(['sh', '-c', 'base64 /dev/urandom | head -c 25'], stdout=subprocess.PIPE).stdout.decode('utf-8')

        msg = f"""```
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@    WARNING: REMOTE HOST IDENTIFICATION HAS CHANGED!     @
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
IT IS POSSIBLE THAT SOMEONE IS DOING SOMETHING NASTY!
Someone could be eavesdropping on you right now (man-in-the-middle attack)!
It is also possible that a host key has just been changed.
The fingerprint for the ED25519 key sent by the remote host is
SHA256:{randomstring}.
Please contact your system administrator.
Add correct host key in /home/doingus/.ssh/known_hosts to get rid of this message.
Offending ED25519 key in /home/doingus/.ssh/known_hosts:{random.randint(1, 420)}
Host key for {random.randint(1, 255)}.{random.randint(1, 255)}.{random.randint(1, 255)}.{random.randint(1, 255)} has changed and you have requested strict checking.
Host key verification failed.
```"""

        await ctx.send(msg)

    @text.command('stallman', 'Sends the GNU/Linux interjection copypasta. You can replace \'Linux\' with any word you want.', ['interject'])
    async def stallman(ctx: commands.CommandContext, linux: str = 'Linux'):

        interjection: str = """
I'd just like to interject for a moment. What you're referring to as Linux, is in fact, GNU/Linux, or as I've recently taken to calling it, GNU plus Linux. Linux is not an operating system unto itself, but rather another free component of a fully functioning GNU system made useful by the GNU corelibs, shell utilities and vital system components comprising a full OS as defined by POSIX.

Many computer users run a modified version of the GNU system every day, without realizing it. Through a peculiar turn of events, the version of GNU which is widely used today is often called Linux, and many of its users are not aware that it is basically the GNU system, developed by the GNU Project.

There really is a Linux, and these people are using it, but it is just a part of the system they use. Linux is the kernel: the program in the system that allocates the machine's resources to the other programs that you run. The kernel is an essential part of an operating system, but useless by itself; it can only function in the context of a complete operating system. Linux is normally used in combination with the GNU operating system: the whole system is basically GNU with Linux added, or GNU/Linux. All the so-called "Linux" distributions are really distributions of GNU/Linux."""

        await ctx.reply(interjection.replace("Linux", linux))

    return text