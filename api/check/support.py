import disnake as discord
import json
from disnake.ext import commands


def moderator():
    def wrapper(ctx):
        with open('data/access/staff.json') as f:
            moderator = json.load(f)
        if ctx.author.id in moderator:
            return True
        raise commands.MissingPermissions('Вы не можете использовать эту команду, потому что вы не являетесь персоналом.')
    return commands.check(wrapper)