#!/usr/bin/env python3
'''Module for executing multiple asynchronous tasks and returning sorted results.
'''
import asyncio
from typing import List

# Importing the task_wait_random function from the previous module
task_wait_random = __import__('3-tasks').task_wait_random

async def task_wait_n(n: int, max_delay: int) -> List[float]:
    '''Executes task_wait_random n times and returns sorted wait times.
    
    Args:
        n (int): The number of tasks to execute.
        max_delay (int): The maximum delay for each task.
    
    Returns:
        List[float]: A list of wait times in seconds, sorted in ascending order.
    '''
    # Use asyncio.gather to concurrently run n instances of task_wait_random
    wait_times = await asyncio.gather(
        *tuple(map(lambda _: task_wait_random(max_delay), range(n)))
    )
    
    # Return the list of wait times sorted in ascending order
    return sorted(wait_times)