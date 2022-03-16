from datetime import datetime
import disnake as discord
from disnake.ext import commands
from api.server import base


class OnMemberRemove(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_member_remove(self, member):

        if base.user(member) is not None:
            base.send(f"DELETE FROM users WHERE guild = {member.guild.id} AND id = {member.id}")
            
        else:
            pass

def setup(client):
    client.add_cog(OnMemberRemove(client))
