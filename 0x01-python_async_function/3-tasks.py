#!/usr/bin/env python3
'''Module for creating asynchronous tasks from wait_random.
'''
import asyncio

# Importing the wait_random function from the previous module
wait_random = __import__('0-basic_async_syntax').wait_random

def task_wait_random(max_delay: int) -> asyncio.Task:
    '''Creates and returns an asyncio Task for the wait_random coroutine.
    
    Args:
        max_delay (int): The maximum delay in seconds for the wait_random function.
    
    Returns:
        asyncio.Task: An asyncio Task that executes wait_random asynchronously.
    '''
    # Create and return a new asyncio Task for wait_random with the specified max_delay
    return asyncio.create_task(wait_random(max_delay))