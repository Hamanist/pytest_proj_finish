import pytest as pytest

from utils import arrs
import pytest

def test_get():
    assert arrs.get([1, 2, 3], 2, "test") == 3


def test_get_error():
    with pytest.raises(IndexError):
        assert arrs.get([], 0, "test") == "test"


def test_slice():
    assert arrs.my_slice([1, 2, 3, 4], 1, 3) == [2, 3]
    assert arrs.my_slice([1, 2, 3], 1) == [2, 3]
