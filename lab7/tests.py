"""
test for l7_7.py
"""

import unittest

from l7_7 import calculate_delivery_cost


class TestDeliveryCost(unittest.TestCase):
    """
    class for test delivery cost"""

    def setUp(self):
        """
        rates_table = {(0, 1): 0.5, (1, 10): 1.0, (10, 20): 1.5}
        """
        self.rates = {(0, 1): 0.5, (1, 10): 1.0, (10, 20): 1.5}

    def test_normal_delivery(self):
        """
        test normal delivery
        """
        self.assertEqual(calculate_delivery_cost(10, 2, self.rates), 10.0)

    def test_light_package(self):
        """
        test light package"""
        self.assertEqual(calculate_delivery_cost(10, 0.5, self.rates), 5.0)

    def test_heavy_package(self):
        """
        test heavy package
        """
        self.assertEqual(calculate_delivery_cost(10, 15, self.rates), 15.0)

    def test_negative_distance(self):
        """
        test negative distance"""
        self.assertEqual(calculate_delivery_cost(-10, 5, self.rates), 0.0)

    def test_negative_weight(self):
        """
        test negative weight"""
        self.assertEqual(calculate_delivery_cost(10, -5, self.rates), 0.0)

    def test_out_of_bounds_weight(self):
        """
        test out of bounds weight"""
        self.assertEqual(calculate_delivery_cost(10, 25, self.rates), 0.0)


if __name__ == "__main__":
    unittest.main()
