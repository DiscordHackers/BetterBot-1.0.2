import disnake as discord
import json
from disnake.ext import commands


def beta():
    def wrapper(ctx):
        with open('data/access/beta.json') as f:
            beta = json.load(f)
        if ctx.author.id in beta:
            return True
        raise commands.MissingPermissions('Вы не можете использовать эту команду, потому что вы не являетесь бета-тестером.')
    return commands.check(wrapper)