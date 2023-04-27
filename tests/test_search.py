import pytest
from typing import List
from simpleprofile import binary_search, custom_binary_search


@pytest.mark.parametrize(
    "my_list, value, expected",
    [
        ([1, 4, 7, 8, 10], 1, 0),
        ([1, 4, 7, 8, 10], 7, 2),
        ([1, 4, 7, 8, 10], 8, 3),
        ([1, 4, 7, 8, 10], 10, 4),
    ],
)
def test_std_binary(my_list: List[int], value: int, expected: int):
    assert binary_search(my_list, value) == expected


@pytest.mark.parametrize(
    "my_list, value, expected",
    [
        ([1, 4, 7, 8, 10], 1, 0),
        ([1, 4, 7, 8, 10], 7, 2),
        ([1, 4, 7, 8, 10], 8, 3),
        # ([1, 4, 7, 8, 10], 10, 4),
    ],
)
def test_custom_binary(my_list: List[int], value: int, expected: int):
    assert custom_binary_search(my_list, value) == expected
