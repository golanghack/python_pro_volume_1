#! /usr/bin/env python3 

# This program or module is free software: you can redistribute it and/or
# modify it under the terms of the GNU General Public License as published
# by the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version. It is provided for educational
# purposes and is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.


"""<--EXTERNAL SITES-->"""

import sys 
from collections import defaultdict

sites = defaultdict(set)
for filename in sys.argv[1:]:
    with open(filename) as file:
        for line in file:
            i = 0
            while True:
                site = None
                i = line.find("http://", i)
                if i > -1:
                    i += len("http://")
                    for j in range(i, len(line)):
                        if not (line[j].isalnum() or line[j] in ".-"):
                            site = line[i:j].lower()
                            break
                    if site and "." in site:
                        sites[site].add(filename)
                    i = j
                else:
                    break
                
for site in sorted(sites):
    print(f'{site} is refered to in: ')
    for filename in sorted(sites[site], key=str.lower):
        print(f'   {filename}')