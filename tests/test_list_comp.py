from uuid import NIL

import pytest
from practice.list_comp import *


@pytest.mark.parametrize("nums, expected", [
    ([],           []),
    ([2],          [4]),
    ([1, 2, 3],    [1, 4, 9]),
    ([-1, -2, -3], [1, 4, 9]),
    ([-1, 0, 3],   [1, 0, 9]),
])
def test_squares(nums, expected):
    assert squares(nums) == expected

@pytest.mark.parametrize("nums, expected", [
    ([],           []),
    ([2],          [2]),
    ([1, 2, 3],    [2]),
    ([-1, -2, -3], [-2,]),
    ([-1, 0, 3, 5, 8, 8],   [0, 8 ,8]),
])
def test_keepevens(nums, expected):
    assert keepevens(nums) == expected

@pytest.mark.parametrize("nums, expected", [
    ([1, 2, 3, 'a'], [1, 2, 3]),
    ([],           []),
    (["a","b","c"],[]),
    ([1.5,2.0,3,(5/2)],[3]),
    ([True, False, None, 1, 0, 5, 6], [1,0,5,6])
])
def test_keepints(nums, expected):
    assert keepints(nums) == expected

@pytest.mark.parametrize("nums, expected", [
    ([], []),
    ([1, 2, 3], [1, 3]),
    ([-1, -2, 0, -10, 5], [-1, 5])
])
def test_keepodd(nums, expected):
    assert keepodd(nums) == expected
