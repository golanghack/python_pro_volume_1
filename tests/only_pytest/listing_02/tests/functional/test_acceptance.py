#! /usr/bin/env python3

from src.fizzbuzz import fizzbuzz

def test_fizzbuzz(capsys):
    numbers = range(20)

    fizzbuzz(numbers)