#!/usr/bin/python3
"""s"""
import json


def load_from_json_file(filename):
    """s"""
    with open(filename) as f:
        return (json.load(f))
