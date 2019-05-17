#!/usr/bin/env python3

"""
Run the baby sitter kata

Simulate a baby sitter working for an evening and getting paid for their hours according to a sliding scale
"""


from sitter import Sitter, convert_to_european, convert_from_european
from family import Family, MINIMUM_START, MAXIMUM_END, FAMILY_A_RATES, FAMILY_B_RATES, FAMILY_C_RATES

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Sit Baby.")
    parser.add_argument("start")
    parser.add_argument("end")
    args = parser.parse_args()

    start_time = convert_from_european(int(args.start))
    if start_time < MINIMUM_START:
        raise Exception("Error: Can't start before {}:00".format(MINIMUM_START))
    end_time = convert_from_european(int(args.end))
    if end_time < start_time:
        end_time = convert_from_european(int(args.end), True)
    if end_time > MAXIMUM_END:
        raise Exception("Error: Can't work past {}:00".format(convert_to_european(MAXIMUM_END)))

    print("Babysitter starts at: {}:00 and finishes at: {}:00".format(args.start, args.end))

    familyA = Family(FAMILY_A_RATES)
    familyB = Family(FAMILY_B_RATES)
    familyC = Family(FAMILY_C_RATES)

    sitter = Sitter(start_time, end_time - start_time, familyA)
    sitter_payment = sitter.calculate_payment()
    print("Sitter payment: ${}".format(sitter_payment))
