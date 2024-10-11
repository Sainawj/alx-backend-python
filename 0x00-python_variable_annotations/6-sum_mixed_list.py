#!/usr/bin/env python3
"""
This module defines a function that calculates the sum of a mixed list 
containing both integers and floats, returning the result as a float.
"""
from typing import List, Union

def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Compute the sum of a list containing both integers and floats.
    
    Args:
        mxd_lst (List[Union[int, float]]): A list of integers and floats.
        
    Returns:
        float: The total sum of the numbers in the list, as a float.
    """
    return sum(mxd_lst)