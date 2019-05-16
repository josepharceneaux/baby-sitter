"""
Tests for baby sitter kata
"""


import unittest

from ..sitter import Sitter
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
        self.sitter = Sitter(sitter_start_time, self.hours_worked, self.family)

    def test_family_creation(self):
        """
        Test correct creation of Family object
        """

    def test_sitter_creation(self):
        """
        Test correct creation of sitter object
        """

    def test_convert_to_european(self):
        """
        Test converstion from absolute hours to European time format
        """

    def test_convert_from_european(self):
        """
        Test converstion from absolute hours to European time format
        """

    def test_sitter_payment(self):
        """
        Test correct calculation of sitter payment
        """
