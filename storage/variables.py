import ruamel.yaml

yaml = ruamel.yaml.YAML(typ='safe')
yaml.indent(offset=2)
with open('configuration/config.yaml', 'r') as f:
    data = yaml.load(f)
   

clientid = data["clientid"]
guildid = data["guildid"]
token = data["token"]
status_message = data["status"]
todo = data["todo"]
finished = data["finished"]
welcome = data["welcome_channel"]