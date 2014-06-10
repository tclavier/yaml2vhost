yaml2vhost
==========

Build apache vhost with proxypass and cache from yaml in python

Sample yaml configuration file :

    "subdomain1.domain.com":
      servers: ['prod1', 'prod2', 'qual1', 'dev2']
      context: subDomain1
      port: 8080
    "subdomain2.domain.com":
      servers: ['prod1', 'prod2', 'qual1', 'dev2']
      context: subDomain2
      cache: disk
      port: 9080

Sample vhost generated
    
    <VirtualHost *:*>
      ProxyPreserveHost On
      ProxyPass /subDomain1 http://localhost:8080/subDomain1
      ProxyPassReverse /subDomain1 http://localhost:8080/subDomain1
      ServerName subdomain1.domain.com
    </VirtualHost>"

    <VirtualHost *:*>
      ProxyPreserveHost On
      ProxyPass /subDomain2 http://localhost:9080/subDomain2
      ProxyPassReverse /subDomain2 http://localhost:9080/subDomain2
      ServerName subdomain2.domain.com
      CacheEnable disk /
    </VirtualHost>"

