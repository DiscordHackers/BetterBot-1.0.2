from datetime import datetime
import disnake as discord
from disnake.ext import commands, tasks
from api.server import base


class OnReady(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        await self.client.change_presence(activity = discord.Activity(type = discord.ActivityType.watching, name = f"help | client"))
        print("ptero start")

        for guild in self.client.guilds:
            if base.guild(guild) is None:
                base.send(f"INSERT INTO config VALUES ('{guild.id}', 'ru')")
            else:
                pass

        for guild in self.client.guilds:           
            for member in guild.members:
                if not member.bot:
                    try:
                        if base.user(member) is None:
                            base.send(f"INSERT INTO users VALUES ({guild.id}, {member.id}, '{member}', NULL, NULL, 0, NULL)")                         
                        else:
                            pass
                    except:
                        continue            

def setup(client):
    client.add_cog(OnReady(client))