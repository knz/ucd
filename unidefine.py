#! /usr/bin/env python

# Converts the JSON database to a C/C++ header.

import sys
import json

db = json.load(open(sys.argv[1]))

for code, name in db:
    dname = name.replace(' ', '_').replace('-', '_')
    print("#define UC_%s %#x" % (dname, code))
