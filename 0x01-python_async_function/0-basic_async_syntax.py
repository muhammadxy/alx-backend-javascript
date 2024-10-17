#!/usr/bin/env python3

"""
This module contains an implementation of an asynchronous coroutine that
takes an integer arg. that waits for a random delay between 0 and `max_delay`
seconds and eventually returns it.
Hint: Use the random module.
"""

# import asyncio module and random module
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    This function takes an int argument that waits for a random delay between
    0 and `max_delay` seconds and eventually returns it.
    """
    delay: float = random.uniform(0, max_delay)  # get random delay
    await asyncio.sleep(delay)  # wait for delay
    return delay  # return delay
