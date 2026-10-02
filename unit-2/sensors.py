"""Utilities for checking mission sensor readings."""

LIMIT = 72.0


def check_limit(reading):
    """Return True when a sensor reading is above the limit."""
    return reading > LIMIT


def calculate_mean(readings):
    """Return the average of the supplied readings."""
    return sum(readings) / len(readings)


if __name__ == "__main__":
    print("test:", check_limit(80), calculate_mean([12, 18, 24]))