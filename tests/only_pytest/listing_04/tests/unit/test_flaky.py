#! /usr/bin/env python3 

def flaky_appender(l, numbers):
    from multiprocessing.pool import ThreadPool

    with ThreadPool(5) as pool:
        pool.map(lambda n: l.append(n), numbers)

from flaky import flaky 

@flaky
def test_appender():
    l = []
    flaky_appender(l, range(1000))
    assert l == list(range(1000))