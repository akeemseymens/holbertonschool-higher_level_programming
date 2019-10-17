#!/usr/bin/python3
from sys import argv
save_json_file = __import__('7-save_to_json_file').save_to_json_file
load_json_file = __import__('8-load_from_json_file').load_from_json_file

filename = "add_item.json"

try:
    my_list = load_json_file(filename)
except FileNotFoundError:
    my_list = []

for num in range(1, len(argv)):
    my_list.append(argv[num])
save_json_file(my_list, filename)
