#!/usr/bin/env python3

"""
This module contains a function that takes an integer max_delay as argument
and returns asyncio.Task
"""


# import asyncio module
import asyncio
# import wait_random function from `0-basic_async_syntax.py
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int = 10) -> asyncio.Task:
    """
    This function takes an integer max_delay as argument and returns
    asyncio.Task object
    """

    task = asyncio.create_task(wait_random(max_delay))  # create a new task
    return task  # return the task
