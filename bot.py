import disnake as discord
from disnake.ext import commands
from disnake.utils import get
from os import listdir

from api.server.dataIO import fileIO
from api.check import support, utils
from api.server import base

from configs.config import *

# ? ------------------------
# ? | SETUP DISCORD CLIENT |
# ? ------------------------

intents = discord.Intents.default()
intents.presences = True
intents.members = True
intents.guilds = True
intents.messages = True

client = commands.Bot(
    command_prefix = "$",
    help_command = None,
    intents = discord.Intents.all()
)

# ? ----------------
# ? | LOADING COGS |
# ? ----------------
for filename in listdir('./commands/'):
    if filename.endswith('.py'):
        client.load_extension(f'commands.{filename[:-3]}')
    else:
        if (filename != '__pycache__'):
            for file in listdir(f'./commands/{filename}/'):
                if file.endswith('.py'):
                    client.load_extension(f'commands.{filename}.{file[:-3]}')

for filename in listdir('./events/'):
    if filename.endswith('.py'):
        client.load_extension(f'events.{filename[:-3]}')

# ? --------------------
# ? | BOT REGISTRATION |
# ? --------------------

client.run(token)