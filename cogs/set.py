import discord
from discord import app_commands
from discord.app_commands import Choice
from discord.ext import commands

class set(commands.Cog):
  def __init__(self, client: commands.Bot):
    self.client = client

  @app_commands.command(name = "set", description = "Changes a setting")
  @app_commands.choices(setting=[
      Choice(name='Playing status',value='status'),
      Choice(name='To-Do list channel',value='todo'),
      Choice(name='Finished to-do channel',value='finished'),
      Choice(name='Welcome channel',value='welcome_channel'),
  ])

  async def set(self, interaction: discord.Interaction, setting: str, value: str):
      try:
          original_value = None
          with open('./configuration/config.yaml', 'r') as f:
              for line in f:
                  if line.startswith(f'{setting}:'):
                      original_value = line.split(':', 1)[1].strip()
                      break

          if original_value is None:
              print(f"Key '{setting}' not found in the YAML file.")
          else:
              with open('./configuration/config.yaml', 'r') as f:
                  lines = f.readlines()

              with open('./configuration/config.yaml', 'w') as f:
                  for line in lines:
                      if line.startswith(f'{setting}:'):
                          line = line.replace(original_value, value).replace('<#', '').replace('>', '')
                      f.write(line)

              await interaction.response.send_message('Setting has been updated sucessfully! Restart the bot for changed to take place.')

      except Exception as e:
          await interaction.response.send_message(f'An error has occurred: `{e}`')

async def setup(client:commands.Bot) -> None:
  await client.add_cog(set(client))