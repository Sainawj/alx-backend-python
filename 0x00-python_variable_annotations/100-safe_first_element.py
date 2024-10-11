#!/usr/bin/env python3
"""This module provides a function with duck-typed annotations to safely retrieve the first element of a sequence."""

from typing import Any, Union, Sequence

def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    Return the first element of a sequence or None if the sequence is empty.
    
    Args:
        lst (Sequence[Any]): A sequence (like a list or tuple) from which to retrieve the first element.
        
    Returns:
        Union[Any, None]: The first element of the sequence or None if the sequence is empty.
    """
    return lst[0] if lst else None