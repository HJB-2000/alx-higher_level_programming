#!/usr/bin/python3
"""cript that adds all arguments to a Python list,
        and then save them to a file"""
import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = \
        __import__('6-load_from_json_file').load_from_json_file
# Load existing items from the file or create an empty list
try:
    items_list = load_from_json_file("add_item.json")
except FileNotFoundError:
    items_list = []

# Add new items from command line arguments
items_list.extend(sys.argv[1:])

# Save the updated list to the file
save_to_json_file(items_list, "add_item.json")
