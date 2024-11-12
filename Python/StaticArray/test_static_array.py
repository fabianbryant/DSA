#!/usr/bin/env python3

import pytest

static_array = __import__('static_array', globals(), locals(), [], 0)
from static_array import StaticArray


array = StaticArray(capacity=10)


def test_static_array_insert_end():
    # Insert end with array not full
    for i in range(2, 21, 2):
        array.insertEnd(value=i)

    assert array.array == [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

    # Insert end with array full, should do nothing
    array.insertEnd(value=1000)

    assert array.array == [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]


def test_static_array_remove_end():
    # Remove end with elements in array
    for _ in range(5):
        array.removeEnd()

    assert array.array == [2, 4, 6, 8, 10, 0, 0, 0, 0, 0]

    for _ in range(5):
        array.removeEnd()

    assert array.array == [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    # Remove end with no elements in array, should do nothing
    array.removeEnd()

    assert array.array == [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]


def test_static_array_insert():
    # Insert within range
    for i in range(50, 9, -10):
        array.insert(index=0, value=i)

    assert array.array == [10, 20, 30, 40, 50, 0, 0, 0, 0, 0]

    array.insert(index=1, value=15)
    array.insert(index=3, value=25)
    array.insert(index=5, value=35)
    array.insert(index=7, value=45)
    array.insert(index=9, value=55)

    assert array.array == [10, 15, 20, 25, 30, 35, 40, 45, 50, 55]

    # Insert out of range, should do nothing
    array.insert(index=10, value=999)

    assert array.array == [10, 15, 20, 25, 30, 35, 40, 45, 50, 55]


def test_static_array_remove():
    # Remove within range
    for i in range(8, -1, -2):
        array.remove(index=i)

    assert array.array == [15, 25, 35, 45, 55, 0, 0, 0, 0, 0]

    # Remove out of range, should do nothing
    array.remove(index=99)

    assert array.array == [15, 25, 35, 45, 55, 0, 0, 0, 0, 0]


def test_static_array_update():
    # Update with valid index
    value = 0
    for i in range(5):
        array.update(index=i, value=value)
        value += 50

    assert array.array == [0, 50, 100, 150, 200, 0, 0, 0, 0, 0] 

    # Update with invalid index, should do nothing
    array.update(index=1000, value=1337)

    assert array.array == [0, 50, 100, 150, 200, 0, 0, 0, 0, 0]


def test_static_array_get():
    # Get with valid index
    assert array.get(index=4) == 200
    assert array.get(index=3) == 150
    assert array.get(index=2) == 100
    assert array.get(index=1) == 50
    assert array.get(index=0) == 0

    # Get with invalid index
    assert array.get(index=42) is None


def test_static_array_print():
    assert str(array) == '[0, 50, 100, 150, 200, 0, 0, 0, 0, 0]'

