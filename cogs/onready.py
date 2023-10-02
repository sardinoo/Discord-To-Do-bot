import discord
from discord.ext import commands
from storage import variables

class onready(commands.Cog):
  def __init__(self, client: commands.Bot):
    self.client = client


  @commands.Cog.listener()
  async def on_ready(self):
      await self.client.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name=f'{variables.status_message}', status=discord.Status.dnd))
      try:
          synced = await self.client.tree.sync()
          print(f'Synced {str(len(synced))} command(s)')
      except Exception as e:
          print(e)
      print(f"Logged in as {self.client.user}")

async def setup(client:commands.Bot) -> None:
  await client.add_cog(onready(client))