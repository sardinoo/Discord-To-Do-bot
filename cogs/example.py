import discord
from discord import app_commands
from discord.ext import commands

class example(commands.Cog):
  def __init__(self, client: commands.Bot):
    self.client = client

  @app_commands.command(name="example", description="Sends hello!")
  async def cog1(self, interaction: discord.Interaction):
    await interaction.response.send_message(content="Hello!")

async def setup(client:commands.Bot) -> None:
  await client.add_cog(example(client))