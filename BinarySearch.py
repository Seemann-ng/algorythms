from typing import List
import pytest


class Search:
    @staticmethod
    def binarySearch(array: List[int], target: int) -> int or None:
        """
        Search the index of an element, equal to the target value, in the given sorted array by the means
        of the binary search algorythm, if the element is present in the array.
        Args:
            array: The sorted array of values to search in.
            target: The target value of an element of the array, the index of which is to be found.

        Returns:
            The index of the element of the array with the value equal to the target value if such element is present,
            otherwise returns None.
        """
        if not array:
            return None
        value_index = len(array) // 2
        start_index = 0
        stop_index = len(array) - 1
        while True:
            if target == array[value_index]:
                return value_index
            elif target < array[value_index]:
                stop_index = value_index
            elif target > array[value_index]:
                start_index = value_index
            value_index = start_index + (stop_index - start_index) // 2
            if stop_index - start_index <= 1:
                if array[start_index] == target:
                    return start_index
                elif array[stop_index] == target:
                    return stop_index
                else:
                    return None


@pytest.mark.parametrize(
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
def testBinarySearch(array, target, result):
    assert Search.binarySearch(array, target) == result
