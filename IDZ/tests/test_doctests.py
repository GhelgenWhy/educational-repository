"""run doctests."""

import doctest
import sys
import unittest

sys.path.insert(0, "src")

import word_counter  # noqa: E402 pylint: disable=import-outside-toplevel


def load_tests(loader, tests, ignore):
    """load tests."""
    tests.addTests(doctest.DocTestSuite(word_counter))
    return tests


if __name__ == "__main__":
    unittest.main()
