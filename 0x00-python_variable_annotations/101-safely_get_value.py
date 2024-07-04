#!/usr/bin/env python3
'''Task 11 module.
'''


from typing import TypeVar, Dict, Optional

# Define a type variable for the key
K = TypeVar('K')

# Define a type variable for the value
V = TypeVar('V')


def safely_get_value(dct: Dict[K, V], key: K, default:
                     Optional[V] = None) -> Optional[V]:
    if key in dct:
        return dct[key]
    else:
        return default
