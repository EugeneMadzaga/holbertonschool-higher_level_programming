#!/usr/bin/python3
"""Script that adds all arguments to a Python list"""
import sys
import os.path
import json


save_file = __import__('5-save_to_json_file').save_to_json_file
load_file = __import__('6-load_from_json_file').load_from_json_file

my_list = []
if os.path.exists("7-add_item.json"):
    my_list = load_file("7-add_item.json")

for arg in sys.argv[1:]:
    my_list.append(arg)

save_file(my_list, "7-add_item.json")
