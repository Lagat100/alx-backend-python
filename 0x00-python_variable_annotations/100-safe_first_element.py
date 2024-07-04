#!/usr/bin/env python3
'''Task 10.
'''

from typing import Optional, Any

def safe_first_element(lst: list) -> Optional[Any]:
    if lst:
        return lst[0]
    else:
        return None

