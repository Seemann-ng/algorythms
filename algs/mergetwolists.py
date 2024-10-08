from typing import List

import pytest


class Merge:
    @staticmethod
    def two_sorted_lists(list1: List[int], list2: List[int]) -> List[int]:
        """Merge two sorted non-decreasing lists into one sorted list containing all elements of given lists.

        Args:
            list1: First sorted in non-decreasing order list.
            list2: Second sorted in non-decreasing order list.

        Returns:
            Sorted in non-decreasing order list consisting all elements of given lists.

        """
        result = []
        list1_index, list2_index = 0, 0
        while list1_index != len(list1) or list2_index != len(list2):
            if list1_index == len(list1) or list2_index != len(list2) and list1[list1_index] >= list2[list2_index]:
                result.append(list2[list2_index])
                list2_index += 1
            else:
                result.append(list1[list1_index])
                list1_index += 1
        return result


class TestMerge:
    merge = Merge()
    params = pytest.mark.parametrize(
        "list1,list2,result",
        [
            ([], [], []),
            ([1], [1], [1, 1]),
            ([1], [2], [1, 2]),
            ([1, 1, 2, 3], [1, 2, 4, 5], [1, 1, 1, 2, 2, 3, 4, 5]),
            ([1, 5, 6], [2, 10], [1, 2, 5, 6, 10]),
            ([1, 5, 6, 7], [1, 5, 7, 15, 16], [1, 1, 5, 5, 6, 7, 7, 15, 16]),
            ([1, 2, 4], [1, 3, 4], [1, 1, 2, 3, 4, 4]),
            ([], [0], [0]),
            ([0], [], [0])
        ]
    )

    @params
    def test_merge_two_sorted_lists(self, list1, list2, result):
        assert self.merge.two_sorted_lists(list1, list2) == result
