import numpy as np
from lstspline import ToyClass, StatsClass

def test_sum_after_set_values():
    tc = ToyClass(5)
    vals = [1.5, 2.5, 3.5, 4.5, 5.5]
    tc.set_values(vals)
    result = tc.sum()
    print("Return size of object",tc.size)
    print("\nTest: sum_after_set_values")
    print("Values:", vals)
    print("Calculated sum:", result)

def test_sum_incremental_updates():
    tc = ToyClass(4)
    print("\nTest: sum_incremental_updates")
    print("Initial sum:", tc.sum())
    tc.set_value(0, -1.0)
    tc.set_value(1, 1.0)
    tc.set_value(2, 2.0)
    tc.set_value(3, -2.0)
    result = tc.sum()
    print("Updated values:", tc.get_values())
    print("Calculated sum:", result)

def test_sum_large_values():
    tc = ToyClass(3)
    big = 1e100  # safe large number
    tc.set_value(0, big)
    tc.set_value(1, big)
    tc.set_value(2, -big)
    result = tc.sum()
    print("\nTest: sum_large_values")
    print("Values:", tc.get_values())
    print("Calculated sum:", result)


def test_get_value_single():
    """Test retrieving individual values using get_value."""
    tc = ToyClass(5)
    for i in range(5):
        tc.set_value(i, i + 1.0)  

    print("\nTest: get_value_single")
    for i in range(5):
        val = tc.get_value(i)
        print(f"Index {i}: Retrieved {val}")

def test_stats_func():
    tc = ToyClass(15)
    tc.set_values([11,22,33,45,33,45,6,7,8,9,33,45,77,55,22,])
    print("\nTest: test_stats_func")
    sc = StatsClass(tc)
    print("mean: ", sc.mean(), "Median: ",sc.median(), "Mode: ",sc.mode())

def test_get_values_array():
    """Test retrieving all values at once using get_values."""
    values = [5.5, 4.4, 3.3, 2.2, 1.1]
    tc = ToyClass(5)
    tc.set_values(values)

    retrieved = tc.get_values()
    print("\nTest: get_values_array")
    print("Retrieved values:", retrieved)

if __name__ == "__main__":
    test_get_value_single()
    test_get_values_array()
    test_sum_after_set_values()
    test_sum_incremental_updates()
    test_sum_large_values()
    test_stats_func()

