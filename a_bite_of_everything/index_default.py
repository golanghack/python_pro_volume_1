#! /usr/bin/env python3 

import collections
import re 
import sys 

WORD = re.compile(r'\w+')
index = collections.defaultdict(list)

with open(sys.argv[1], encoding='utf-8') as file_input:
    for line_no, line in enumerate(file_input, 1):
        for match in WORD.finditer(line):
            word = match.group()
            column_no = match.start() + 1 
            location = (line_no, column_no)
            index[word].append(location)

for word in sorted(index, key=str.upper):
    print(word, index[word])