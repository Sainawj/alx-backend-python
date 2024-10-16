#!/usr/bin/env python3
'''This module defines an asynchronous generator that produces a sequence of random numbers.
'''
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    '''Asynchronously generates a sequence of 10 random floating-point numbers.

    The function waits for 1 second between generating each number, and yields a random 
    float between 0 and 10.

    Returns:
        Generator[float, None, None]: A generator that yields random floats.
    '''
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.random() * 10