from typing import List

import pytest


class Search:
    @staticmethod
    def binary_search(array: List[int], target: int) -> int or None:
        """Search index of target in sorted array with binary search algorythm, if the element is present in the array.

        Args:
            array: Sorted array to search in.
            target: Target item of array, the index of which is to be found.

        Returns:
            Index of item of the array with value equal to the target if such is present, otherwise returns None.

        """
        if not array:
            return None
        value_index = len(array) // 2
        start_index = 0
        stop_index = len(array) - 1
        while True:
            if target < array[value_index]:
                stop_index = value_index
            elif target > array[value_index]:
                start_index = value_index
            else:
                return value_index
            value_index = start_index + (stop_index - start_index) // 2
            if stop_index - start_index <= 1:
                if array[start_index] == target:
                    return start_index
                elif array[stop_index] == target:
                    return stop_index
                return None


class TestSearch:
    search = Search()
    params = pytest.mark.parametrize(
        "array,target,result",
        [
            ([], 1, None),
            ([1], 0, None),
            ([1], 1, 0),
            ([1, 1, 3], 3, 2),
            ([1, 1, 3], 1, 0 or 1),
            ([1, 2, 3, 4], 5, None),
            ([1, 2, 3], 0, None),
            ([0, 2, 3, 5, 6, 7], 0, 0),
            ([1, 2, 3, 4, 5, 5, 6, 7, 8], 3, 2),
            ([1, 3, 4, 5, 6, 7, 8], 7, 5),
            ([12, 167, 8900], 12, 0),
            ([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 8, 8),

        ]
    )

    @params
    def test_binary_search(self, array, target, result):
        assert self.search.binary_search(array, target) == result
