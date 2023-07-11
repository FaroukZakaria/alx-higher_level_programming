#!/usr/bin/python3
"""s"""
import json


def save_to_json_file(my_obj, filename):
    """s"""
    with open(filename, 'w') as f:
        json.dump(my_obj, f)
