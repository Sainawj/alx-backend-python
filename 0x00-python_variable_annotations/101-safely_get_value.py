#!/usr/bin/env python3
"""This module defines a method to safely retrieve a value from a dictionary."""

from typing import Mapping, Any, Union, TypeVar, Optional

T = TypeVar('T')

def safely_get_value(dct: Mapping, key: Any, default: Optional[T] = None) -> Union[Any, T]:
    """
    Safely retrieve a value from a dictionary.
    
    Args:
        dct (Mapping): The dictionary from which to retrieve the value.
        key (Any): The key for which to get the value.
        default (Optional[T]): The value to return if the key is not found (defaults to None).
        
    Returns:
        Union[Any, T]: The value associated with the key if found, otherwise the default value.
    """
    return dct.get(key, default)