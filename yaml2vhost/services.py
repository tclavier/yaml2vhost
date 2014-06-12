import yaml, sys
from string import Template

class Services:
    def build(self, yml, host):
        env = yaml.load(yml)
        output = ""
        for name in env:
            if host in env[name]['servers']:
                template = Template("http://$host:$port/$context $container:$version\n")
                replace = dict(
                    context   = env[name]['context'], 
                    port      = env[name]['port'],
                    container = env[name]['container'],
                    version   = env[name]['version'],
                    host      = host
                    )

                output += template.substitute(replace)
        return output
