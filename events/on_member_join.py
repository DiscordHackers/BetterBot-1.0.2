from datetime import datetime
import disnake as discord
from disnake.ext import commands
from disnake.utils import get
from api.server import base


class OnMemberJoin1(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_member_join(self, member):

        if not member.bot:
            if base.user(member) is None:
                base.send(f"INSERT INTO users VALUES ('{member.guild.id}', '{member.id}', {member}, NULL, NULL, 0, NULL)")           
            else:
                pass

def setup(client):
    client.add_cog(OnMemberJoin1(client))