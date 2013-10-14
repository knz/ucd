#! /usr/bin/env python

# Converts the Unicode Character Database "Name list" format
# to JSON.

import sys

db = []
for n in open(sys.argv[1]):
    n = n.rstrip()
    if n.startswith('@') or n.startswith(';') or n.startswith('\t'):
        # ignore comments and continuation lines
        continue
    else:
        a,b = n.split('\t',1)
        name = b.strip()
        if name.startswith("<"):
            # ignore special characters
            continue
        code = int(a, 16)

        db.append( (code, name) )

# write database to JSON.
import json
of = open(sys.argv[2], 'w')
json.dump(db, of)
of.close()
