#!/usr/bin/python
import sys
sys.path.append('.')
from yaml2vhost import *

if len(sys.argv) == 2 :
    action = 'vhost'
    host = sys.argv[1]
else:
    if len(sys.argv) == 3:
        action = sys.argv[1]
        host = sys.argv[2]
    else:
        print >> sys.stderr, "bad number of params"
        sys.exit(2)

if action not in ['vhost','services']:
    print >> sys.stderr, "bad action : " + action
    sys.exit(3)

data = sys.stdin.read()

if action == 'vhost':
    obj = vhost.Vhost()
else:
    obj = services.Services()

out = obj.build(data,host)
if len(out) < 1:
    sys.exit(1)
else:
    print out
