#!/usr/bin/env python

import json

# goal
protein=212
fat=52
carb=139

with open("may_23_2017", "rU") as f:
    for line in f.readlines():
        row = json.loads(line.strip())
        row[1] = carb - row[1]
        row[2] = fat - row[2]
        row[3] = protein - row[3]
        print(row)
