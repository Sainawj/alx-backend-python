#!/usr/bin/env python3
"""This module defines a function with annotated parameters and return types."""

from typing import Iterable, Sequence, List, Tuple

def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Return a list of tuples, each containing a sequence and its length.
    
    Args:
        lst (Iterable[Sequence]): An iterable containing sequences.
        
    Returns:
        List[Tuple[Sequence, int]]: A list of tuples, where each tuple contains
        a sequence and its corresponding length.
    """
    return [(i, len(i)) for i in lst]