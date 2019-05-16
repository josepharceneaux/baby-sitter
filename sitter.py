"""
Class for a baby sitter
"""



def convert_to_european(time):
    """
    Convert a fixed number of hours into European time format
    """
    return time % 24


def convert_from_european(time, next_day=False):
    """
    Given a European time format (0-23) convert into the total number of hours
    """
    if next_day:
        return time + 24

    return time

class Sitter:
    """
    The payment due a sitter based upon the hours worked and the family they worked for
    """

    def __init__(self, start_time, hours_worked, family):
        """
        Constructor for Sitter class
        """

        self.start_time = start_time
        self.hours_worked = hours_worked
        self.family = family

    def calculate_payment(self):
        """
        Calculate the total amount due to this sitter based upon a family's hourly rates
        """
