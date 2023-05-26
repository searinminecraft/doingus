import voltage
from voltage.ext import commands
import sys
from math import floor

def setup(client) -> commands.Cog:
    utility = commands.Cog(
        name = 'Utilities',
        description = 'Some useful stuff'
    )

    @utility.command('avatar', 'yoinks someone\'s avatar :cat_steal:', ['av', 'pfp'])
    async def avatar(ctx: commands.CommandContext, user: voltage.Member = None):
        if user is None:
            user = ctx.author

        if user.avatar is None:
            avatar = await user.default_avatar.get_binary()
        else:
            avatar = await user.avatar.get_binary()

        f = voltage.File(f = avatar, filename = user.avatar.name if user.avatar else user.default_avatar.name)

        embed = voltage.SendableEmbed(
            title = f'{user.name}\'s beautiful avatar',
            color = "#f5a9b8",
            media = f
        )

        await ctx.send(embeds=[embed])

    @utility.command('banner', 'yoink someone\'s banner :cat_steal:')
    async def banner(ctx: commands.CommandContext, user: voltage.Member = None):
        if user is None:
            user = ctx.author

        profile = await user.fetch_profile()
        if profile.background is None:
            return await ctx.reply(f'User {user.name} does not have a banner!')

        await ctx.reply(embed=voltage.SendableEmbed(
            title = f'{user.name}\'s beautiful banner',
            media = voltage.File(f = await profile.background.get_binary(), filename = profile.background.name),
            icon_url = user.avatar.url if user.avatar else user.default_avatar.url,
            color = '#f5a9b8'
        ))

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

    @utility.command('whois', 'Get user information')
    async def whois(ctx: commands.CommandContext, user: voltage.Member = None):
        if user is None:
            user = ctx.author

        embed = voltage.SendableEmbed(
            title = f'User Information for {user.name}',
            description = f"""**Name**: {user.name}
            **Created At**: <t:{floor(user.created_at / 1000)}:F>, <t:{floor(user.created_at / 1000)}:R>
            **ID**: `{user.id}`
            **Bot**: {"Yes" if user.bot else 'No'}
            **Avatars**: [[Avatar]]({user.avatar.url}?max_side=256) | [[Avatar (Full)]]({user.avatar.url}) | [[Default Avatar]]({user.default_avatar.url})""",
            color = '#f5a9b8',
            icon_url = user.avatar.url
        )

        await ctx.send(embed=embed)

    @utility.command('bio', 'Get a user\'s profile bio.', ['description'])
    async def description(ctx: commands.CommandContext, user: voltage.Member = None):
        if user is None:
            user = ctx.author

        profile = await user.fetch_profile()
        if profile.content is None:
            return await ctx.reply(f'User {user.name} does not have a bio set!')

        await ctx.reply(embed=voltage.SendableEmbed(
            title = f'{user.name}\'s bio',
            description = profile.content,
            icon_url = user.avatar.url if user.avatar else user.default_avatar.url,
            color = '#f5a9b8'
        ))

    @utility.command('serverinfo', 'Get server information.')
    async def serverinfo(ctx: commands.CommandContext):
        server = ctx.server
        await ctx.reply(
            embed=voltage.SendableEmbed(
                title = f'Server information for {server.name}',
                description = f"""**Name**: {server.name}
**Creation Date**: <t:{floor(server.created_at[0] / 1000)}:F>, <t:{floor(server.created_at[0] / 1000)}:R>
**Owner**: <@{server.owner_id}> ({server.owner.name})
**NSFW**: {"Yes" if server.nsfw else "No"}
**ID**: `{server.id}`
**Members**: {len(server.members)}""",
                icon_url = server.icon.url if server.icon else (client.user.avatar.url if client.user.avatar else client.user.default_avatar.url),
                color = '#f5a9b8'
            )
        )


    return utility
