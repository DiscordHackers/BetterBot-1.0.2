import disnake
from disnake.ext import commands
from api.server import base, main
import random

# Define a simple View that gives us a confirmation menu
class Confirm(disnake.ui.View):
    def __init__(self):
        super().__init__()
        self.value = None

    @disnake.ui.button(label="Принять", style=disnake.ButtonStyle.green)
    async def confirm(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
        await interaction.response.send_message("Выполнено!", ephemeral=True)
        self.value = True
        self.stop()

    @disnake.ui.button(label="Отмена", style=disnake.ButtonStyle.grey)
    async def cancel(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
        await interaction.response.send_message("Отмена?.. Жалко....", ephemeral=True)
        self.value = False
        self.stop()

class Test(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_role("clan key")
    async def create(self, ctx: commands.Context, *, name):
        try:
            if base.user(ctx.author)[5] == 1:
                await ctx.send(embed=main.deny(ctx.guild, main.get_lang(ctx.guild, "ERROR1")))
            elif base.user(ctx.author)[3] is not None:
                await ctx.send(embed=main.deny(ctx.guild, main.get_lang(ctx.guild, "ERROR2")))
            elif name == base.clan(ctx.guild)[1]:
                await ctx.send(embed=main.deny(ctx.guild, main.get_lang(ctx.guild, "ERROR8")))
            else:    
                view = Confirm()
                embed=main.warn(ctx.guild, main.get_lang(ctx.guild, "CREATE_CONFIRM").format(name))
                await ctx.send(embed=embed, view=view)
                await view.wait()
                if view.value is None:
                    pass
                elif view.value:
                    valuee = random.randint(1, 10000)
                    guild = ctx.guild
                    await guild.create_role(name=f"{name}")
                    role = disnake.utils.get(ctx.guild.roles, name=f"{name}")
                    base.send(f"INSERT INTO clans VALUES ('{ctx.guild.id}', '{name}', '{valuee}', '{role.id}', '{ctx.author.id}')")
                    await ctx.author.add_roles(role)
                    base.send(f"UPDATE users SET clan = '{name}', clanid = '{valuee}', own = 1, clanown = '{ctx.author.id}' WHERE guild = '{ctx.guild.id}' AND id = '{ctx.author.id}'")
                else:
                    pass
        except:
            if base.user(ctx.author)[5] == 1:
                await ctx.send(embed=main.deny(ctx.guild, main.get_lang(ctx.guild, "ERROR1")))
            elif base.user(ctx.author)[3] is not None:
                await ctx.send(embed=main.deny(ctx.guild, main.get_lang(ctx.guild, "ERROR2")))
            else:    
                view = Confirm()
                embed=main.warn(ctx.guild, main.get_lang(ctx.guild, "CREATE_CONFIRM").format(name))
                await ctx.send(embed=embed, view=view)
                await view.wait()
                if view.value is None:
                    pass
                elif view.value:
                    valuee = random.randint(1, 10000)
                    guild = ctx.guild
                    await guild.create_role(name=f"{name}")
                    role = disnake.utils.get(ctx.guild.roles, name=f"{name}")
                    base.send(f"INSERT INTO clans VALUES ('{ctx.guild.id}', '{name}', '{valuee}', '{role.id}', '{ctx.author.id}')")
                    await ctx.author.add_roles(role)
                    base.send(f"UPDATE users SET clan = '{name}', clanid = '{valuee}', own = 1, clanown = '{ctx.author.id}' WHERE guild = '{ctx.guild.id}' AND id = '{ctx.author.id}'")
                else:
                    pass            

    @commands.command()
    async def delete(self, ctx: commands.Context):
        if base.user(ctx.author)[6] != ctx.author.id:
            await ctx.send(embed=main.deny(ctx.guild, main.get_lang(ctx.guild, "ERROR3")))
        elif base.user(ctx.author)[3] is None:
            await ctx.send(embed=main.deny(ctx.guild, main.get_lang(ctx.guild, "ERROR4")))
        else:
            view = Confirm()
            embed = main.warn(ctx.guild, main.get_lang(ctx.guild, "DELETE_CONFIRM").format(base.user(ctx.author)[3]))
            await ctx.send(embed=embed, view=view)
            await view.wait()
            if view.value is None:
                pass
            elif view.value:
                role = disnake.utils.get(ctx.guild.roles, name=f"{base.user(ctx.author)[3]}")
                await role.delete()
                base.send(f"DELETE FROM clans WHERE clan = '{base.user(ctx.author)[3]}' AND guild = '{ctx.guild.id}'")
                base.send(f"UPDATE users SET clan = NULL, clanid = NULL, own = 0, clanown = NULL WHERE clan = '{base.user(ctx.author)[3]}' AND guild = '{ctx.guild.id}'")                
            else:
                pass          

    @commands.command()
    async def clan(self, ctx: commands.Context):
        if base.user(ctx.author)[3] is None:
            await ctx.send(embed=main.deny(ctx.guild, main.get_lang(ctx.guild, "ERROR4")))
        else:
            role = disnake.utils.get(ctx.guild.roles, name=f"{base.user(ctx.author)[3]}")
            await ctx.send(embed=disnake.Embed(title=f"Информация о {base.user(ctx.author)[3]}", description=f"\n Участников: {len(role.members)} \n ID-клана: **{base.user(ctx.author)[4]}** \n Владелец клана: <@{base.user(ctx.author)[6]}>")) 

    @commands.command()
    async def invite(self, ctx: commands.Context, member: disnake.Member):
        def check(msg):
            return msg.author != ctx.author and msg.author == member
        if base.user(ctx.author)[6] != ctx.author.id:
            await ctx.send(embed=main.deny(ctx.guild, main.get_lang(ctx.guild, "ERROR3")))
        elif base.user(ctx.author)[3] is None:
            await ctx.send(embed=main.deny(ctx.guild, main.get_lang(ctx.guild, "ERROR4")))
        elif base.user(member)[5] == 1:
            await ctx.send(embed=main.deny(ctx.guild, main.get_lang(ctx.guild, "ERROR6")))
        elif base.user(member)[3] is not None:
            await ctx.send(embed=main.deny(ctx.guild, main.get_lang(ctx.guild, "ERROR5")))
        else:
            view = Confirm()
            embed = main.warn(ctx.guild, main.get_lang(ctx.guild, "INVITE_CONFIRM").format(member.mention, base.user(ctx.author)[3]))
            await ctx.send(embed=embed, view=view)
            await view.wait()
            if view.value is None:
                pass
            elif view.value:
                await ctx.send(f"{member.mention}")
                await ctx.send(embed=main.warn(ctx.guild, main.get_lang(ctx.guild, "INVITE_MSG").format(ctx.author.mention, base.user(ctx.author)[3])))
                response = await self.bot.wait_for("message", check=check)
                if response.content.lower().strip() == "да" or response.content.lower().strip() == "Да" or response.content.lower().strip() == "ДА":
                    if base.user(member)[5] == 1:
                        await ctx.send(embed=main.deny(ctx.guild, main.get_lang(ctx.guild, "ERROR6")))
                    elif base.user(member)[3] is not None:
                        await ctx.send(embed=main.deny(ctx.guild, main.get_lang(ctx.guild, "ERROR5")))
                    else:                    
                        await ctx.send(embed=main.done(ctx.guild, main.get_lang(ctx.guild, "INVITE_SUCCESS").format(member.mention, base.user(ctx.author)[3])))
                        role = disnake.utils.get(ctx.guild.roles, name=f"{base.user(ctx.author)[3]}")
                        await member.add_roles(role)
                        base.send(f"UPDATE users SET clan = '{base.user(ctx.author)[3]}', clanid = '{base.user(ctx.author)[4]}', clanown = '{ctx.author.id}' WHERE id = {member.id} AND guild = {ctx.guild.id}")
                else:
                    await ctx.send(embed=main.done(ctx.guild, main.get_lang(ctx.guild, "INVITE_DENY").format(member.mention, base.user(ctx.author)[3])))
            else:
                pass    

    @commands.command()
    async def kick(self, ctx: commands.Context, member: disnake.Member):
        if base.user(ctx.author)[6] != ctx.author.id:
            await ctx.send(embed=main.deny(ctx.guild, main.get_lang(ctx.guild, "ERROR3")))
        if base.user(member)[5] == 1:
            await ctx.send(embed=main.deny(ctx.guild, main.get_lang(ctx.guild, "ERROR6")))
        elif base.user(member)[3] != base.user(ctx.author)[3]:
            await ctx.send(embed=main.deny(ctx.guild, main.get_lang(ctx.guild, "ERROR10")))
        elif base.user(member)[3] is None:  
            await ctx.send(embed=main.deny(ctx.guild, main.get_lang(ctx.guild, "ERROR9"))) 
        else:
            view = Confirm()
            embed = main.warn(ctx.guild, main.get_lang(ctx.guild, "KICK_CONFIRM").format(member.mention, base.user(ctx.author)[3]))
            await ctx.send(embed=embed, view=view)
            await view.wait()
            if view.value is None:
                pass
            elif view.value:
                if base.user(ctx.author)[6] != ctx.author.id:
                    await ctx.send(embed=main.deny(ctx.guild, main.get_lang(ctx.guild, "ERROR3")))                
                if base.user(member)[5] == 1:
                    await ctx.send(embed=main.deny(ctx.guild, main.get_lang(ctx.guild, "ERROR6")))
                elif base.user(member)[3] != base.user(ctx.author)[3]:
                    await ctx.send(embed=main.deny(ctx.guild, main.get_lang(ctx.guild, "ERROR10")))
                elif base.user(member)[3] is None:  
                    await ctx.send(embed=main.deny(ctx.guild, main.get_lang(ctx.guild, "ERROR9"))) 
                else:                    
                    await ctx.send(embed=main.done(ctx.guild, main.get_lang(ctx.guild, "KICK_SUCCESS").format(member.mention, base.user(ctx.author)[3])))
                    role = disnake.utils.get(ctx.guild.roles, name=f"{base.user(ctx.author)[3]}")
                    await member.remove_roles(role)
                    base.send(f"UPDATE users SET clan = NULL, clanid = NULL, clanown = NULL WHERE id = {member.id} AND guild = {ctx.guild.id}")
            else:
                pass    


def setup(bot):
    bot.add_cog(Test(bot))