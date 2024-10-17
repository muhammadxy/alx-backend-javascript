#!/usr/bin/env python3

"""
This module contains an async routine that takes in 2 int arguments and returns
the list of all the delays between the two numbers.
The list should be in ascending order.
"""

# import asyncio module
import asyncio
from typing import List
# import wait_random function from `0-basic_async_syntax.py`
wait_random = __import__('0-basic_async_syntax').wait_random


# define `wait_n` async function with n and max_delay as arguments
async def wait_n(n: int, max_delay: int = 10) -> List[float]:
    """ Waits for ran delay until max_delay, returns list of actual delays """
    spawn_list = []  # list of coroutines to spawn later on the process
    delay_list = []  # list of delays to return later on the process
    for i in range(n):  # spawn n coroutines to wait for random delays
        # create coroutine to wait for random delay
        delayed_task = asyncio.create_task(wait_random(max_delay))
        # add callback to add delay to list of delays
        delayed_task.add_done_callback(lambda x: delay_list.append(x.result()))
        spawn_list.append(delayed_task)

    for spawn in spawn_list:  # wait for all coroutines to finish
        await spawn

    return delay_list  # return list of delays
