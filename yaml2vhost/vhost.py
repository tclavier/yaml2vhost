import yaml, sys
from string import Template

class Vhost:
    def build(self, yml, host):
        env = yaml.load(yml)
        output = ""
        for name in env:
            if host in env[name]['servers']:
                template = Template("""
<VirtualHost *:*>
    ProxyPreserveHost On
    ProxyPass /$context http://localhost:$port/$context
    ProxyPassReverse / http://192.168.111.2/
    ServerName $name
</VirtualHost>"
""")
                output += template.substitute(
                    context = env[name]['context'], 
                    port    = env[name]['port'],
                    name    = name)
        return output
