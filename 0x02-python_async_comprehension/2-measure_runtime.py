#!/usr/bin/env python3
'''This module defines a function to measure the execution time
of running an asynchronous comprehension multiple times.
'''
import asyncio
import time
from importlib import import_module as using

# Import async_comprehension from the previous module
async_comprehension = using('1-async_comprehension').async_comprehension

async def measure_runtime() -> float:
    '''Measures the total execution time for running async_comprehension 4 times.

    This function asynchronously executes the async_comprehension function 4 times
    in parallel using asyncio.gather(), and calculates the total time taken for the 
    entire operation.

    Returns:
        float: The total time taken to execute async_comprehension 4 times.
    '''
    start_time = time.time()  # Record the start time
    # Run async_comprehension 4 times concurrently
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    return time.time() - start_time  # Calculate and return the elapsed time