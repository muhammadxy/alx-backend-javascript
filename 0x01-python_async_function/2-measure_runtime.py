#!/usr/bin/env python3

"""
This module contains a function with integers n and max_delay as arguments
that measures the total execution time for wait_n(n, max_delay), and returns
tottal_time / n.
Returns a float.
Hint: Use the time module to measure an approximate elapsed time.
"""

# import asyncio module and time module
import asyncio
import time
# import wait_n function from `1-concurrent_coroutines.py`
wait_n = __import__('1-concurrent_coroutines').wait_n


# define measure_time function with n and max_delay as arguments
def measure_time(n: int, max_delay: int = 10) -> float:
    """
    Measures the total execution time for wait_n(n, max_delay), and returns
    tottal_time / n.
    Returns a float.
    """
    start_time = time.time()  # start timer for total execution time
    asyncio.run(wait_n(n, max_delay))  # run wait_n function
    # stop timer for total execution time for wait_n function
    elapsed_time = time.time() - start_time
    return elapsed_time / n  # return total execution time divided by n
