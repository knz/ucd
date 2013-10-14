#! /usr/bin/env python

# Converts the JSON database to text (requires Unicode support).

import sys
import json

db = json.load(open(sys.argv[1]))

for code, name in db:
    print("%#8x  %-10s %s" % (code,chr(code), name))
