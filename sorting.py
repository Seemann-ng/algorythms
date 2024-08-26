from typing import List
import pytest


class Sorting:
    @staticmethod
    def selectionSort(array: List[int]) -> List[int]:
        for value1_index in range(len(array)):
            current_smallest_value = array[value1_index]
            current_smallest_value_index = value1_index
            for value2_index in range(value1_index + 1, len(array)):
                if array[value2_index] < current_smallest_value:
                    current_smallest_value = array[value2_index]
                    current_smallest_value_index = value2_index
            array[value1_index], array[current_smallest_value_index] = current_smallest_value, array[value1_index]
        return array

    @classmethod
    def quickSort(cls, array: List[int]) -> List[int]:
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
        return cls.quickSort(less) + equal + cls.quickSort(greater)


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
    def testSelectionSort(self, array, result):
        assert self.sorting.selectionSort(array) == result

    @params
    def testQuickSort(self, array, result):
        assert self.sorting.quickSort(array) == result
