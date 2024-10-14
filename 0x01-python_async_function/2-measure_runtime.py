#!/usr/bin/env python3
'''Module for measuring the average execution time of asynchronous tasks.
'''
import asyncio
import time

# Importing the wait_n function from the previous module
wait_n = __import__('1-concurrent_coroutines').wait_n

def measure_time(n: int, max_delay: int) -> float:
    '''Measures the average execution time of wait_n.
    
    This function calculates the total time taken to execute the asynchronous 
    wait_n function and returns the average time per call.
    
    Args:
        n (int): The number of times to call wait_random via wait_n.
        max_delay (int): The maximum delay in seconds for each wait_random call.
    
    Returns:
        float: The average time taken per call of wait_n.
    '''
    # Record the start time
    start_time = time.time()
    
    # Run the asynchronous wait_n function and wait for it to complete
    asyncio.run(wait_n(n, max_delay))
    
    # Calculate the total elapsed time and return the average time per execution
    total_time = time.time() - start_time
    return total_time / n