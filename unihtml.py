#! /usr/bin/env python

# Converts the JSON database to HTML.

import sys
import json

db = json.load(open(sys.argv[1]))

print("""<html>
<head>
<title>Unicode code points and names</title>
<style type=text/css>
.c  { display: inline-block; width:5em; }
.s  { display: inline-block; font-family: serif; width:2em; }
.sf { display: inline-block; font-family: sans-serif; width:2em; }
.m  { display: inline-block; font-family: monospace; width:2em; }
</style>
<body>
<p>
""")

for code, name in db:
    print("<span class=c>%X</span>" % code)
    print("<span class=s>&#x%X;</span>" % code)
    print("<span class=sf>&#x%X;</span>" % code)
    print("<span class=m>&#x%X;</span>" % code)
    print("<span>%s</span><br />" % name)

print("</p></body></html>")
