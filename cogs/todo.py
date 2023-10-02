import discord
from discord.ext import commands
from storage import variables
from cogs import buttons

class todo(commands.Cog):
  def __init__(self, client: commands.Bot):
    self.client = client

  @commands.Cog.listener()
  async def on_message(self, message):
    if message.author.bot:
      return
    if str(message.channel.id) == str(variables.todo):
      await message.delete()
      em = discord.Embed(title=f'New to-do from {message.author.name}', description=message.content, color= discord.Color.blue())
      em.set_footer(text='click ✅ once this has been completed')
      await message.channel.send(embed=em, view=buttons.buttons.ctodo())
    else:
      return

async def setup(client:commands.Bot) -> None:
  await client.add_cog(todo(client))