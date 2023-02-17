#! /usr/bin/env python3

import os.path

PATHS = [
    '/one/two/three', 
    '/one/two/three/',
    '/', 
    '.', 
    '',
] 

for path in PATHS:
    print(f'{path!r:>17} -> {os.path.split(path)}')

