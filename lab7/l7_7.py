"""
delivery app
"""


def calculate_delivery_cost(distance: float, weight: float, rates: dict) -> float:
    """
    calculate delivery cost

    >>> rates_table = {(0, 1): 0.5, (1, 10): 1.0, (10, 20): 1.5}
    >>> calculate_delivery_cost(10.0, 2.0, rates_table)
    10.0
    >>> calculate_delivery_cost(10.0, 0.5, rates_table)
    5.0
    >>> calculate_delivery_cost(-5.0, 2.0, rates_table)
    0.0
    >>> calculate_delivery_cost(10.0, 25.0, rates_table)
    0.0
    """
    if distance < 0 or weight < 0:
        return 0.0

    rate_multiplier = 0.0
    for (min_w, max_w), rate in rates.items():
        if min_w <= weight < max_w:
            rate_multiplier = rate
            break

    return float(distance * rate_multiplier)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
