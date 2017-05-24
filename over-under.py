#!/usr/bin/env python

import json
import sys

# goal
protein=212
fat=52
carb=139

if len(sys.argv) < 2:
    print >> sys.stderr, "No path given"
    print >> sys.stderr, "Usage: over-under.py [path]"
    sys.exit(1)

path = sys.argv[1]

with open(path, "rU") as f:
    for line in f.readlines():
        row = json.loads(line.strip())
        row[1] = row[1] - carb
        row[2] = row[2] - fat
        row[3] = row[3] - protein
        print("%s\t%s\t%s\t%s" % (row[0], row[1], row[2], row[3]))
