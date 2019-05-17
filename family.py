"""
Class and functions for a family a baby sitter might work for
"""


# Fallback for rate
DEFAULT_MINIMUM_RATE = 20

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
        n_rates = len(rates)
        if n_rates < 1 :
            raise Exception("Rates entered must be >= 1, but is {}".format(n_rates))
        if n_rates > 11:
            raise Exception("Can't have more than 11 hours but {} were submitted".format(n_rates))

        self.start_time = MINIMUM_START
        self.end_time = MAXIMUM_END
        self.default_rate = DEFAULT_MINIMUM_RATE
        self.rate_dict = self.slice_rates(rates)

    def slice_rates(self, rates):
        """
        Create a dict of all hours a sitter might work and the rate for each hour
        """

        # Presumes rates only increase over time
        rate_dict = {}
        previous_rate = DEFAULT_MINIMUM_RATE
        for time in range(MINIMUM_START, MAXIMUM_END):
            if time in rates:
                current_rate = rates[time]
                rate_dict[time] = current_rate
            else:
                rate_dict[time] = current_rate

        return rate_dict
