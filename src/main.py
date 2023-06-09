import voltage
from dotenv import load_dotenv, dotenv_values, set_key
from utils.log import log, color
from voltage.ext import commands
import random
import json
import asyncio
import os
import aiohttp
import subprocess
import xml.etree.ElementTree as et

load_dotenv()
REVOLT_TOKEN = dotenv_values()['revolt_token']
PREFIX = dotenv_values()['prefix']

class MyHelpCommand(commands.HelpCommand):
    async def send_help(self, ctx: commands.CommandContext):
        embed = voltage.SendableEmbed(
            title="Help",
            description=f"Use `{ctx.prefix}help <command>` to get help for a command.",
            colour="#f5a9b8",
            icon_url=ctx.author.display_avatar.url
        )
        text = "\n### **No Category**\n"
        for command in self.client.commands.values():
            if command.cog is None:
                text += f"> {command.name}\n"
        for i in self.client.cogs.values():
            text += f"\n### **{i.name}**\n{i.description}\n"
            for j in i.commands:
                text += f"\n> {j.name}"
        if embed.description:
            embed.description += text
        return await ctx.reply(f"[]({ctx.author.id})", embed=embed)

client = commands.CommandsClient(PREFIX, help_command=MyHelpCommand)

@client.error('message')
async def on_error(error:Exception, message:voltage.Message):
    if isinstance(error, voltage.CommandNotFound):
        embed = voltage.SendableEmbed(
            title = 'Well, that was unexpected...',
            description = f'The command you tried to execute ({error.command}) doesn\'t exist you little dingus',
            color = '#f5a9b8' 
        )

        return await message.reply(embeds=[embed])

    if isinstance(error, voltage.NotEnoughArgs):
        embed = voltage.SendableEmbed(
            title = 'Oops, guess you forgot something...',
            description = f'Not enough arguments provided for command {error.command.name}. Expected {error.expected}, got {error.actual}.',
            color = '#f5a9b8' 
        )

        return await message.reply(embeds=[embed])


    if isinstance(error, voltage.NotBotOwner):
        embed = voltage.SendableEmbed(
            title = 'Bro?',
            description = 'You\'re not my bot owner, sussy baka.',
            color = '#f5a9b8'
        )

        return await message.reply(embeds='embed')
    
    if isinstance(error, voltage.MemberNotFound):
        embed = voltage.SendableEmbed(
            title = 'AAAAAAAAAAAAAA',
            description = f'Couldn\'t find user {error.resource}.',
            color = '#f5a9b8'
        )
        
        return await message.reply(embeds=[embed])

    if isinstance(error, voltage.NotEnoughPerms):
        embed = voltage.SendableEmbed(
            title = ':(',
            description = f'You do not have permission to do that. Please make sure you have the `{error.perm}` permission!',
            color = '#f5a9b8'
        )
   
    embed = voltage.SendableEmbed(
        title = 'I\'m sorry, but an error occured!',
        description = f'```\n{type(error)}: {error}\n```',
        color = '#f5a9b8'
    )

    await message.reply(embeds=[embed])    

async def loop():
    for i in range(1, 2147483647):
        statuses = [
            'OwO',
			'Revolt >>>>>>>',
			f'Making {len(client.members)} members smile',
			'kimden is sweet',
			'Watching you!',
			'-help | https://github.com/searinminecraft/doingus',
			f'Random number: {random.randint(1, 10000)}',
			'I love you, and everyone!',
			'aeasus',
            'Simple, fast, systemd-free!',
            f'Python Powered! Voltage {voltage.__version__}'
		]
		
        status = random.choice(statuses)
        await client.set_status(status, voltage.PresenceType.online)

        await asyncio.sleep(120)

@client.listen('message')
async def on_message(message: voltage.Message):
    
    if isinstance(message.channel, voltage.DMChannel):
        log('Chat', f'[{message.author.name}]: {message.content}', color.CYAN)
    else:
        log('Chat', f'[{message.author.name} | {message.channel.name} | {message.server.name}]: {message.content}', color.CYAN)
    if message.author.bot:
        if message.author.id == '01FHGJ3NPP7XANQQH8C2BE44ZY': # Allow AutoMod, for bridged messages.
            pass
        else:
            return

    if message.content == f"<@{client.user.id}>":
        embed = voltage.SendableEmbed(
            title = 'You pinged me! OwO',
            description = f'My prefix is `{client.prefix}`',
            color = '#f5a9b8'
        )

        return await message.channel.send(embed=embed)

    if message.content.lower() == 'aea':
        return await message.reply('aeasus')

    if message.content.lower() == 'hi':
        return await message.reply(f'hi {message.author.name}')

    if message.content.lower() == f'i love {client.user.name}':
        return await message.reply('I love you too!')

    if message.content.lower() == f'i hate {client.user.name}':
        return await message.reply("I can't believe you would say that to me! :sob:")

    await client.handle_commands(message)

@client.listen('ready')
async def on_ready():
    print(f"""{color.PURPLE}{color.BOLD}
                        .
                       ...'      .''....''.,;;,;'.       ...'
                        ,  .,..:'.              ..',,.  ...',
                        '.  'c.                      ,l:' ..,
                        ...'.                          .;:...
                         ;,                              .l.
                         c                                .,
                        ;.       ... ..  .......           ;'
                        l     ...   ......     ...... .     o
                       ',  ...     .;              ..  ...  ;.
                       c...  .'    ,'                  .. ..,;
                       ' ...;'    '. .                   ,'  '
                       .lc.c.    .c    ...                '...
                      'd' c      c        .. ..            ;:
                     'l .c      .;                ...  ...'.:,.
                    .o  c       ;                        .:. ;l.
                   .l  ;.       ;      ...               .o   l:
                   :' .l       ..   .,c' ..  '.',:,      .l   ,l
                  ',' .l.      '    c.    . :    ..      .:   .c,      +----------------------------------------------------------------------------+
                  ':.  :l     ..    . .Ol . 'c,  .       .,   .;,      |  doingus - The cutest and most feature rich Revolt bot made with Voltage.  |
                 .c.   .:,    ..    . 'o;. .oOc  .       .'   ..:      |                                                                            |
                ..;    ;  ;.   '    ..   .   .....       '     ',      |  Source Code: https://github.com/searinminecraft/doingus                   |
                .;     ..  ,.  ,                         c     .l      +----------------------------------------------------------------------------+
               .c       ,.   . .  ..             ..     ;.     .:.
              .,.        ..            .        ..     ,'       ;,
              c;                        ......       .'.        .,
             l;.                                 ..             .:.
            ,c.                   ....      ....                 ..           .. ..
            ''.                    ,.  ....    .                 .'        .  ......'
           .;;                   'l:.  ..   . .,c                 ''       .     ;.'.
            .,              . ..':',' ,. .. .'.......:'...'.       ,.       .     ...
             .'..   .....  oo .     ....            .l. ..  .''     ..      .      .
                .;..      .x'                     ..  ..       ;,  ...    .  ....';
               ..        ..  ...            ..      ..          ,,.       ;.....   ,
             '.               .   . ..          ...              ,.      :       ,'
           .,                     ...........                    'l     ,.      .;
           ;                                                      o'   ''       l
          ;.                                                      :,.  c       c
         .l                                                       .l' '.      ,,
         ;,                                                        ;:,l       d
         :.         .                                    .,         co.      ::
         ;.        .                                      ..        .o      .l.
         c.        ,                                       c         .      :;
{color.END}""")

    log(client.user.name, f'Logged in as {client.user.name}! OwO', color.GREEN)
    log('Cogs', 'Loading Cogs...', color.RED)
    client.add_extension('cogs.owner')
    client.add_extension('cogs.fun')
    client.add_extension('cogs.misc')
    client.add_extension('cogs.mc')
    client.add_extension('cogs.text')
    client.add_extension('cogs.image')
    client.add_extension('cogs.utility')
    client.add_extension('cogs.games')
    log('Cogs', 'Successfully Loaded Cogs.', color.RED)

    asyncio.create_task(loop())

client.run(REVOLT_TOKEN)
