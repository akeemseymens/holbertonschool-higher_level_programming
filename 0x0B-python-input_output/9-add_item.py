#!/usr/bin/python3
"""

"""


import sys
save_json = __import__('7-save_to_json_file').save_to_json_file
load_json = __import__('8-load_from_json_file').load_from_json_file

listn = []
try:
    listn = load_json("add_item.json")
except:
    listn = []
elements = len(sys.argv)
for numbers in range(1, elements):
    listing.append(sys.argv[numbers])
save_json(listn, "add_item.json")
