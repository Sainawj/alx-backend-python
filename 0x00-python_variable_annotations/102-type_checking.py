#!/usr/bin/env python3
"""
This module defines a function that returns a list of integers
multiplied by a specified factor.
"""
from typing import Tuple, List

def zoom_array(lst: Tuple[int, ...], factor: int = 2) -> List[int]:
    """
    Create a list of integers, each repeated by a specified factor.
    
    Args:
        lst (Tuple[int, ...]): A tuple of integers to be multiplied.
        factor (int): The number of times to repeat each integer (default is 2).
        
    Returns:
        List[int]: A list containing integers, each multiplied by the specified factor.
    """
    zoomed_in: List[int] = [
        item for item in lst
        for _ in range(factor)
    ]
    return zoomed_in

# Example tuple of integers
array: Tuple[int, ...] = (12, 72, 91)

# Creating zoomed arrays with different factors
zoom_2x = zoom_array(array)
zoom_3x = zoom_array(array, 3)