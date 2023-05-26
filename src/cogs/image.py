import voltage
from voltage.ext import commands
import aiohttp
import random

headers = {'User-Agent': 'Mozilla/5.0 (compatible; doingus/1.0.0; +https://github.com/searinminecraft/doingus)'}

def setup(client) -> commands.Cog:
    image = commands.Cog(
        name = 'Image',
        description = 'Image related commands'
    )

    @image.command('waifu', 'Get a random image from the waifu.pics API')
    async def waifu(ctx: commands.CommandContext, category: str = 'waifu'):

        categories = [
            'waifu',
            'neko',
            'shinobu',
            'megumin',
            'bully',
            'cuddle',
            'cry',
            'hug',
            'awoo',
            'kiss',
            'lick',
            'pat',
            'smug',
            'bonk',
            'yeet',
            'blush',
            'smile',
            'highfive',
            'handhold',
            'nom',
            'bite',
            'glomp',
            'slap',
            'kill',
            'kick',
            'happy',
            'wink',
            'poke',
            'dance',
            'cringe',
            'randomcategory'
        ]

        selected = category

        if category not in categories:
            embed = voltage.SendableEmbed(
                title = 'Oops!',
                description = f"""That's not a valid category!! Possible categories are:

```
{', '.join(categories)}
```""",
                color = '#f5a9b8'
            )

            return await ctx.send(embed=embed)

        if category == 'randomcategory':
            selected = random.choice(categories)
            await ctx.send(f'**Category: {selected}**')

        async with aiohttp.ClientSession(headers=headers) as session:
            async with session.get(f'https://api.waifu.pics/sfw/{selected}') as resp:
                data = await resp.json()


        await ctx.send(f'![]({data.get("url")})')

    @image.command('nwaifu', 'Same as `waifu`, but NSFW.')
    async def nwaifu(ctx: commands.CommandContext):
        if isinstance(ctx.channel, voltage.DMChannel):  # Allow DM channels, because nobody will see them anyway
            pass
        elif ctx.channel.nsfw:
            pass
        else:
            return await ctx.reply(embed=voltage.SendableEmbed(
                title = 'Not so fast!',
                description = 'This channel is not NSFW.',
                color = '#f5a9b8'
            ))

        async with aiohttp.ClientSession(headers=headers) as session:
            async with session.get(f'https://api.waifu.pics/nsfw/waifu') as resp:
                data = await resp.json()


        await ctx.send(f'![]({data.get("url")})')

    return image
