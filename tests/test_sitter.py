"""
Tests for baby sitter kata
"""


import unittest

from ..sitter import Sitter, convert_to_european, convert_from_european
from ..family import Family, MINIMUM_START, MAXIMUM_END, FAMILY_B_RATES


class TestBabySitter(unittest.TestCase):
    """
    Tests for baby sitter kata
    """

    def setUp(self):
        """
        Prepare for tests.
        """

        self.maximum_work_hours = MAXIMUM_END - MINIMUM_START
        self.sitter_start_time = 17
        self.hours_worked = 3
        self.family = Family(FAMILY_B_RATES)
        self.sitter = Sitter(self.sitter_start_time, self.hours_worked, self.family)

    def test_family_creation(self):
        """
        Test correct creation of Family object
        """
        self.assertTrue(self.maximum_work_hours == 11)
        self.assertTrue(len(self.family.rate_dict) == 11)

    def test_sitter_creation(self):
        """
        Test correct creation of sitter object
        """
        self.assertTrue(self.sitter.start_time == self.sitter_start_time)
        self.assertTrue(self.sitter.default_rate == self.family.default_rate)

    def test_convert_to_european(self):
        """
        Test converstion from absolute hours to European time format
        """
        absolute = 27
        self.assertTrue(convert_to_european(absolute) == 3)

    def test_convert_from_european(self):
        """
        Test converstion from absolute hours to European time format
        """
        absolute = 17
        self.assertTrue(convert_from_european(absolute) == 17)

    def test_sitter_payment(self):
        """
        Test correct calculation of sitter payment
        """
        self.assertTrue(self.sitter.calculate_payment() == 3 * 15)
