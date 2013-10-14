#! /usr/bin/env python

# Converts the JSON database to a Python module.

import sys
import json

db = json.load(open(sys.argv[1]))

print("names = {}")
for code, name in db:
    dname = name.replace(' ', '_').replace('-', '_')
    print("%s = u'\\x%x'; names[%#x] = '%s'" % (dname, code, code, name))
