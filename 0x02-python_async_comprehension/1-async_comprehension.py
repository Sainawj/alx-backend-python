#!/usr/bin/env python3
'''This module defines an asynchronous comprehension function to collect
random numbers generated asynchronously.
'''
from typing import List
from importlib import import_module as using

# Import the async_generator function from the previous module
async_generator = using('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    '''Asynchronously collects 10 random numbers from the async generator.

    The function uses asynchronous comprehension to retrieve 10 floating-point
    numbers generated by the async_generator.

    Returns:
        List[float]: A list of 10 random floating-point numbers.
    '''
    return [num async for num in async_generator()]
