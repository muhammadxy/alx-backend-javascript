#!/usr/bin/env python3


"""
This module contains a alter code from previously module that used an
`wait_n` async function.
"""

from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int = 10) -> List[float]:
    """ Waits for ran delay until max_delay, returns list of actual delays """
    spawn_list = []  # list of coroutines to spawn later on the process
    delay_list = []  # list of delays to return later on the process
    for i in range(n):  # spawn n coroutines to wait for random delays
        # create coroutine to wait for random delay
        delayed_task = task_wait_random(max_delay)
        # add callback to add delay to list of delays
        delayed_task.add_done_callback(lambda x: delay_list.append(x.result()))
        spawn_list.append(delayed_task)

    for spawn in spawn_list:  # wait for all coroutines to finish
        await spawn

    return delay_list  # return list of delays
