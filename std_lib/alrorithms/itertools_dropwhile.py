#! /usr/bin/env python3 

from itertools import * 

def should_drop(x: int):
    print('Testing -> ', x)
    return x < 1

for i in dropwhile(should_drop, [-1, 0, 1, 2, -2]):
    print('Yielding -> ', i)