import discord
from discord.ext import commands
from storage import variables


class events(commands.Cog):
  def __init__(self, client: commands.Bot):
    self.client = client

  @commands.Cog.listener()
  async def on_member_join(self, member):
    try:
      channel = self.client.get_channel(int(variables.welcome))
      em = discord.Embed(title=f'Welcome to {member.guild.name}', description=f"Welcome `{member.name}` to **{member.guild.name}**", colour = discord.Colour.blue())
      em.set_thumbnail(url=member.guild.icon.url)
      em.set_footer(text=f'Member count: {len([x for x in member.guild.members if not x.bot])}', icon_url=member.guild.icon.url)
      await channel.send(embed=em)
    except Exception as e:
      print(e)

  @commands.Cog.listener()
  async def on_member_remove(self, member):
    try:
      channel = self.client.get_channel(variables.welcome)
      await channel.send(f'{member.name} left, sadge :(')
    except Exception as e:
      print(e)

async def setup(client:commands.Bot) -> None:
  await client.add_cog(events(client))