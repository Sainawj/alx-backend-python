#!/usr/bin/env python3
'''Module for executing multiple asynchronous wait operations.
'''
import asyncio
from typing import List

# Importing the wait_random function from the previous module
wait_random = __import__('0-basic_async_syntax').wait_random

# Asynchronous function that calls wait_random n times and returns sorted wait times
async def wait_n(n: int, max_delay: int) -> List[float]:
    '''Executes wait_random n times, waits asynchronously, and returns the sorted wait times.
    
    Args:
        n (int): The number of times to call wait_random.
        max_delay (int): The maximum delay in seconds for each wait_random call.
    
    Returns:
        List[float]: A list of wait times in seconds, sorted in ascending order.
    '''
    # Create a list of asyncio tasks by calling wait_random n times and use asyncio.gather to run them concurrently
    wait_times = await asyncio.gather(
        *tuple(map(lambda _: wait_random(max_delay), range(n)))
    )
    
    # Return the sorted list of wait times
    return sorted(wait_times)