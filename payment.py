#!/usr/bin/env python3

"""
Run the baby sitter kata

Simulate a baby sitter working for an evening and getting paid for their hours according to a sliding scale
"""


from sitter import Sitter
from family import Family

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Sit Baby.")
    parser.add_argument("start")
    parser.add_argument("end")
    args = parser.parse_args()

    print("Baby sitter kata")
