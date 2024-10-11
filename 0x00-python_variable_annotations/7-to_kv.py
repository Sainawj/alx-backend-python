#!/usr/bin/env python3
"""This module defines a function that converts a Python variable to a key-value (KV) pair."""
from typing import Union, Tuple

def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Create a key-value (KV) pair where the value is the square of the input number.
    
    Args:
        k (str): The key as a string.
        v (Union[int, float]): The value, either an integer or float.
        
    Returns:
        Tuple[str, float]: A tuple where the key is the input string and the value is the square of the number.
    """
    return k, v ** 2