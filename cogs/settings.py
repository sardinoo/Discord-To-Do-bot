import discord
from discord import app_commands
from discord.ext import commands
from storage import variables

class settings(commands.Cog):
  def __init__(self, client: commands.Bot):
    self.client = client

  @app_commands.command(name = "settings", description = "shows the current settings")

  async def settings(self, interaction: discord.Interaction):
    try:
        em = discord.Embed(title='Bot settings', color=discord.Color.blue())
        em.set_thumbnail(url=interaction.guild.icon.url)
        em.add_field(name='Status message', value=variables.status_message, inline=False)
        em.add_field(name='To-Do list', value=f'<#{variables.todo}>', inline=False)
        em.add_field(name='Finished to-do', value=f'<#{variables.finished}>', inline=False)
        em.add_field(name='Welcome channel', value=f'<#{variables.welcome}>', inline=False)
        
        await interaction.response.send_message(embed=em)
    except Exception as e:
        await interaction.response.send_message(f'An error has occurred: `{e}`')

async def setup(client:commands.Bot) -> None:
  await client.add_cog(settings(client))