from django.test import TestCase


from app.calc import add, subtract


class CalcTests(TestCase):

    def test_add_numbers(self):
        """ Test that the two numbers are correctly added """
        self.assertEqual(add(3, 5), 8)

    def test_subtract_numbers(self):
        """Test that two numbers are subtracted correctly"""
        self.assertEqual(subtract(3, 9), 6)
