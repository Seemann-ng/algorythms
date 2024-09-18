from typing import List

import pytest

from mergetwolists import Merge


class Sorting:
    @staticmethod
    def selection_sort(array: List[int]) -> List[int]:
        """Use selection sort algorythm to sort list.

        Args:
            array: List to be sorted.

        Returns:
            Sorted list.

        """
        for first_index in range(len(array)):
            current_smallest_value = array[first_index]
            current_smallest_value_index = first_index
            for second_index in range(first_index + 1, len(array)):
                if array[second_index] < current_smallest_value:
                    current_smallest_value = array[second_index]
                    current_smallest_value_index = second_index
            array[first_index], array[current_smallest_value_index] = current_smallest_value, array[first_index]
        return array

    def quick_sort(self, array: List[int]) -> List[int]:
        """Use quick sort algorythm to sort list.

        Args:
            array: List to be sorted.

        Returns:
            Sorted list.

        """
        if len(array) < 2:
            return array
        pivot = array[len(array) // 2]
        less, equal, greater = [], [], []
        for value in array:
            if value < pivot:
                less.append(value)
            elif value > pivot:
                greater.append(value)
            else:
                equal.append(value)
        return self.quick_sort(less) + equal + self.quick_sort(greater)

    def merge_sort(self, array: List[int]) -> List[int]:
        """Use merge sort algorythm to sort list.

        Args:
            array: List to be sorted.

        Returns:
            Sorted list.

        """
        if len(array) <= 1:
            return array
        middle_index = len(array) // 2
        subarray1, subarray2 = array[:middle_index], array[middle_index:]
        return Merge.two_sorted_lists(self.merge_sort(subarray1), self.merge_sort(subarray2))


class TestSorting:
    sorting = Sorting()
    params = pytest.mark.parametrize(
        "array,result",
        [
            ([8, 5, 1, 3, 6, 5], [1, 3, 5, 5, 6, 8]),
            ([], []),
            ([5, 5, 5], [5, 5, 5]),
            ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5])
        ]
    )

    @params
    def test_selection_sort(self, array, result):
        assert self.sorting.selection_sort(array) == result

    @params
    def test_quick_sort(self, array, result):
        assert self.sorting.quick_sort(array) == result

    @params
    def test_merge_sort(self, array, result):
        assert self.sorting.merge_sort(array) == result
