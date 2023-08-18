#! /usr/bin/env python3 

import collections

c = collections.Counter()
with open('/usr/share/dict/words', 'rt', encoding='utf-8') as f:
    for line in f:
        c.update(line.rstrip().lower())

print('Most common ->')
for letter, count in c.most_common(3):
    print(f'{letter} -> {count:>7}')