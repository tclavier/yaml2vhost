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
    ProxyPassReverse /$context http://localhost:$port/$context
    ServerName $name
    $cacheLine
</VirtualHost>
""")            
                if 'cache' in env[name]:
                    cache_line = "CacheEnable %s /" % env[name]['cache']
                else :
                    cache_line = ""

                replace = dict(
                    context   = env[name]['context'], 
                    port      = env[name]['port'],
                    name      = name,
                    cacheLine = cache_line
                    )

                output += template.substitute(replace)
        return output
