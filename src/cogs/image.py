import voltage
from voltage.ext import commands
import aiohttp
import random

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
{categories}
```""",
                color = '#f5a9b8'
            )

            return await ctx.send(embed=embed)

        if category == 'randomcategory':
            selected = random.choice(categories if type == 'sfw' else categoriesnsfw)

        data: dict = None

        async with aiohttp.ClientSession() as session:
            async with session.get(f'https://api.waifu.pics/sfw/{selected}') as resp:
                data = await resp.json()


        await ctx.send(f'![]({data.get("url")})')


    return image
