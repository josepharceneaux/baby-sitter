"""
Class and functions for a family a baby sitter might work for
"""


# Earliest a baby sitter may begin work.
MINIMUM_START = 17

# Latest a baby sitter may end work. 28 = 24 + 4, e.g., 4am
MAXIMUM_END = 28

# Start times and associated rates for 3 families. E.g., Family A pays $15/hr from 5pm (17:00) until 11pm and then pays $20
FAMILY_A_RATES = { 17:15, 23:20 }
FAMILY_B_RATES = { 17:15, 22:8, 24:16 }
FAMILY_C_RATES = { 17:21, 21:15 }


class Family:
    """
    A class representing a family
    """

    def __init__(self, rates):
        """
        Constructor for a babysitter family class
        """
