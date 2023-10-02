import discord
from discord.ext import commands
from storage import variables

class buttons(commands.Cog):
  def __init__(self, client: commands.Bot):
    self.client = client

  class ctodo(discord.ui.View):
      def __init__(self):
          super().__init__(timeout=None)
      @discord.ui.button(label='✅', custom_id='tick', style= discord.ButtonStyle.green)
      async def tick(self, interaction: discord.Interaction, Button: discord.ui.Button):
        await interaction.message.delete()
        em = discord.Embed(title=f'{interaction.user.name} has finished something in todo!', description=interaction.message.embeds[0].description, color=discord.Color.blue())
        channel = interaction.guild.get_channel(variables.finished)
        await channel.send(embed=em)

async def setup(client:commands.Bot) -> None:
  await client.add_cog(buttons(client))