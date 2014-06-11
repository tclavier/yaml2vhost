#!/usr/bin/python
import sys
sys.path.append('.')
from yaml2vhost import *

if len(sys.argv) != 1 :
    host = sys.argv[1]

vhost = vhost.Vhost()
data = sys.stdin.read()
apache = vhost.build(data,host)
if len(apache) < 1:
    sys.exit(1)
else:
    print apache
