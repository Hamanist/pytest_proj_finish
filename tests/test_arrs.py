from utils import arrs
import pytest


def test_get():
    assert arrs.get([1, 2, 3], 2, "test") == 3


def test_get_default():
    assert arrs.get([1, 2, 3], -1, "test") == "test"


def test_get_error():
    with pytest.raises(IndexError):
        assert arrs.get([], 0, "test") == "test"


def test_slice():
    assert arrs.my_slice([1, 2, 3, 4], 1, 3) == [2, 3]
    assert arrs.my_slice([1, 2, 3], 1) == [2, 3]


def test_slice_empty_list():
    assert arrs.my_slice([]) == []


def test_slice_not_zero():
    assert arrs.my_slice([1, 2], -4) != 0


def test_slice_normalized_start():
    assert arrs.my_slice([1, 2, 3, 4], -3, 3) == [2, 3]
