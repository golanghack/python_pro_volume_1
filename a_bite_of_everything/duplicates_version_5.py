#! /usr/bin/env python3

def dup(any_list: list) -> bool:
    """Searchin duplicate in list.
    
    :param -> list -> any list, any len(list).
    :return -> bool.
    """
    
    n_range = len(any_list)
    any_list.sort()
    return any(any_list[i + 1] for i in range(n_range - 1))

