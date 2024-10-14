#!/usr/bin/env python3
'''Module for an asynchronous function that waits for a random delay.
'''
import asyncio
import random

# Asynchronous function that waits for a random delay between 0 and max_delay (default is 10 seconds)
async def wait_random(max_delay: int = 10) -> float:
    '''Waits for a random delay between 0 and max_delay seconds.
    
    Args:
        max_delay (int): The maximum number of seconds to wait (default is 10).
    
    Returns:
        float: The actual delay time waited in seconds.
    '''
    # Generate a random float between 0 and max_delay
    wait_time = random.uniform(0, max_delay)
    
    # Asynchronously wait for the generated delay time
    await asyncio.sleep(wait_time)
    
    # Return the actual wait time
    return wait_time