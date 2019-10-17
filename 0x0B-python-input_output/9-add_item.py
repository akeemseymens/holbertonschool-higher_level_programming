#!/usr/bin/python3
"""

"""


from sys import argv
save_json = __import__('7-save_to_json_file').save_to_json_file
load_json = __import__('8-load_from_json_file').load_from_json_file

filename = "add_item.json"


try:
    listn = load_json(filename)
except FileNotFoundError:
    listn = []

elements = len(sys.argv)

for nums in range(1, elements):
    listing.append(sys.argv[nums])
save_json(listn, filename)
