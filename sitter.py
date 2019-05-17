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
    Represent the sitter
    """

    def __init__(self, start_time, hours_worked, family):
        """
        Constructor for Sitter class. Validate start and end times.
        """
        if start_time < family.start_time:
            raise Exception("Start time {} is earlier than family start time, which is: {}".format(start_time, convert_to_european(family.start_time)))
        self.end_time = start_time + hours_worked 
        if self.end_time > family.end_time:
            raise Exception("End time {} is greater than family end time, which is: {}".format(end_time, convert_to_european(family.end_time)))

        self.start_time = start_time
        self.hours_worked = hours_worked
        self.family = family
        self.default_rate = family.default_rate

    def calculate_payment(self):
        """
        Calculate the total amount due to this sitter based upon a family's hourly rates
        """
        if not self.start_time in self.family.rate_dict:
            raise Exception("Invalid start time {}".format(self.start_time))

        end_time = self.start_time + self.hours_worked
        total = 0
        current_rate = self.default_rate
        for t in self.family.rate_dict:
            if t == self.end_time:
                break
            if self.family.rate_dict[t] != current_rate:
                current_rate = self.family.rate_dict[t]

            total = total + current_rate

        return total
