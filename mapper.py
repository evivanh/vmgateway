#!/usr/bin/python
"""mapper.py"""

import sys

def mapper():

 # Input comes from STDIN (standard input)
    for line in sys.stdin:

        row = line.strip().split("\t")
        # Check for the amount of columns we need
        if len(row) < 5 :
            continue

            salesProduct = row[3]
            productPrice = row[4]

        # Identify variables
            print("{3};{4}".format(salesProduct, productPrice))

mapper()

