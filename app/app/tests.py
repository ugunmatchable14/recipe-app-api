from django.test import TestCase

from app.calc import Add

class CalcTests(TestCase):

    def test_add_numbers(self):
        """ Test that the two numbers are correctly added """
        self.assertEqual(add(3, 5), 8)
