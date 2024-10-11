#!/usr/bin/env python3
"""
This module defines a function that returns a list of integers
multiplied by a specified factor.
"""
from typing import Tuple, List

def zoom_array(lst: List[int], factor: int = 2) -> List[int]:
    """
    Create a list of integers, each repeated by a specified factor.
    
    Args:
        lst (List[int]): A list of integers to be multiplied.
        factor (int): The number of times to repeat each integer (default is 2).
        
    Returns:
        List[int]: A list containing integers, each multiplied by the specified factor.
    """
    zoomed_in: List[int] = [
        item for item in lst
        for _ in range(factor)
    ]
    return zoomed_in


array: List[int] = [12, 72, 91]

zoom_2x = zoom_array(array)

# Ensure the factor is an int
zoom_3x = zoom_array(array, int(3.0))  # Cast float to int for correct type
