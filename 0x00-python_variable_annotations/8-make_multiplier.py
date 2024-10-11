#!/usr/bin/env python3
"""This module defines a function that returns a multiplier function."""

from typing import Callable

def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Create a function that multiplies a float by a given multiplier.
    
    Args:
        multiplier (float): The value by which to multiply floats.
        
    Returns:
        Callable[[float], float]: A function that takes a float and returns 
        its product with the given multiplier.
    """
    
    def multiplier_func(number: float) -> float:
        """Multiply a float by the outer multiplier."""
        return multiplier * number

    return multiplier_func