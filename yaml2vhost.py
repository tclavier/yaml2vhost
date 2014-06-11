#!/usr/bin/python
import sys
sys.path.append('.')
from yaml2vhost import *

vhost = vhost.Vhost()
data = sys.stdin.read()
host = "prod1"
apache = vhost.build(data,host)
print apache
