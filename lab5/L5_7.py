import doctest
import random
import unittest
from datetime import datetime, timedelta


def main():
    for _ in range(1, 11):
        expected_time = get_random_time()
        actual_time = get_random_time()
        print(f"Expected time: {expected_time}, Actual time: {actual_time}")
        if is_late(expected_time, actual_time):
            print(
                f"Oh no, employee is late! Delay in minutes: {calculate_delay_minutes(datetime.strptime(expected_time, '%H:%M'), datetime.strptime(actual_time, '%H:%M'))}"
            )
        else:
            print("Employee is on time!")

    print("\ndoctest")
    failures, tests = doctest.testmod(verbose=False)
    if failures == 0:
        print(f"Successfully tested {tests} tests")

    print("\n\nunittest")
    unittest.main(argv=["first-arg-is-ignored"], exit=False)


def calculate_delay_minutes(expected_time, actual_time):
    """
    Calculate delay in minutes between expected and actual time

    :param expected_time: Expected time
    :param actual_time: Actual time
    :return: Delay in minutes
    >>> calculate_delay_minutes(datetime.strptime("10:00", "%H:%M"), datetime.strptime("09:00", "%H:%M"))
    -60.0
    >>> calculate_delay_minutes(datetime.strptime("09:00", "%H:%M"), datetime.strptime("09:00", "%H:%M"))
    0.0
    >>> calculate_delay_minutes(datetime.strptime("09:00", "%H:%M"), datetime.strptime("10:00", "%H:%M"))
    60.0
    """
    return (actual_time - expected_time).total_seconds() / 60


def is_late(expected_time, actual_time):
    """
    Checks if employee is late

    :param expected_time: Expected time
    :param actual_time: Actual time
    :return: True if employee is late, False otherwise
    >>> is_late(datetime.strptime("10:00", "%H:%M"), datetime.strptime("09:00", "%H:%M"))
    False
    >>> is_late(datetime.strptime("09:00", "%H:%M"), datetime.strptime("09:00", "%H:%M"))
    False
    >>> is_late(datetime.strptime("09:00", "%H:%M"), datetime.strptime("10:00", "%H:%M"))
    True
    """
    return expected_time < actual_time


def get_random_time():
    """
    Generates random time between 08:00 and 12:00

    :return: Random time
    """

    start_time = datetime.strptime("08:00", "%H:%M")
    random_minutes = random.randint(0, 240)
    result_time = start_time + timedelta(minutes=random_minutes)
    return result_time.strftime("%H:%M")


class Test(unittest.TestCase):
    def test_is_late(self):
        self.assertFalse(
            is_late(
                datetime.strptime("10:00", "%H:%M"), datetime.strptime("09:00", "%H:%M")
            )
        )
        self.assertFalse(
            is_late(
                datetime.strptime("09:00", "%H:%M"), datetime.strptime("09:00", "%H:%M")
            )
        )
        self.assertTrue(
            is_late(
                datetime.strptime("09:00", "%H:%M"), datetime.strptime("10:00", "%H:%M")
            )
        )

    def test_calculate_delay_minutes(self):
        self.assertEqual(
            calculate_delay_minutes(
                datetime.strptime("10:00", "%H:%M"), datetime.strptime("09:00", "%H:%M")
            ),
            -60,
        )
        self.assertEqual(
            calculate_delay_minutes(
                datetime.strptime("09:00", "%H:%M"), datetime.strptime("09:00", "%H:%M")
            ),
            0,
        )
        self.assertEqual(
            calculate_delay_minutes(
                datetime.strptime("09:00", "%H:%M"), datetime.strptime("10:00", "%H:%M")
            ),
            60,
        )

    def test_get_random_time(self):
        for _ in range(10):
            self.assertTrue(
                get_random_time() >= "08:00" and get_random_time() <= "12:00"
            )


if __name__ == "__main__":
    main()
