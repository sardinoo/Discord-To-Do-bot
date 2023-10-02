import discord
from discord import app_commands
from discord.ext import commands
import sys


class reboot(commands.Cog):
  def __init__(self, client: commands.Bot):
    self.client = client

  @app_commands.command(name = "reboot", description = "restarts the bot")

  async def reboot(self, interaction: discord.Interaction):
      try:
          await interaction.response.send_message('Bot is restarting!')
          sys.exit()
      except Exception as e:
          await interaction.response.send_message(f'An error has occurred: {e}')

async def setup(client:commands.Bot) -> None:
  await client.add_cog(reboot(client))