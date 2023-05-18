import voltage
from voltage.ext import commands
import sys

def setup(client) -> commands.Cog:
    utility = commands.Cog(
        name = 'Utilities',
        description = 'Some useful stuff'
    )

    @utility.command('avatar', 'yoinks someone\'s avatar :cat_steal:', ['av', 'pfp'])
    async def avatar(ctx: commands.CommandContext, user: voltage.Member = None):
        if user is None:
            user = ctx.author

        avatar = None

        if user.avatar is None:
            avatar = await user.default_avatar.get_binary()
        else:
            avatar = await user.avatar.get_binary()

        f = voltage.File(f=avatar, filename='an avatar')

        embed = voltage.SendableEmbed(
            title = f'{user.name}\'s beautiful avatar',
            color = "#f5a9b8",
            media = f
        )

        await ctx.send(embeds=[embed])

    @commands.is_owner()
    @utility.command('shutdown', 'Shutdown the bot.')
    async def shutdown(ctx: commands.CommandContext):
        await ctx.reply('Shutting down.')
        sys.exit(0)

    @utility.command('owoify', 'Makes the message you reply to owo')
    async def owoify(ctx: commands.CommandContext):
        
        try:
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

    @utility.command('roles', 'See a user\'s roles')
    async def roles(ctx: commands.CommandContext, member: voltage.Member):
        result = ''

        for i in member.roles:
            result += f'* {i}\n'

        embed = voltage.SendableEmbed(
            title = f'{member.name}\'s Roles:',
            description = f'{result if result != "" else "This user does not have any roles!"}',
            icon_url = member.avatar.url,
            color = '#fa89b8'
        )
        
        await ctx.reply(embed=embed)

    return utility
