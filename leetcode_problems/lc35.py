from typing import List

import pytest


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        """Search index of target in given array.

        Args:
            nums: Array to search in.
            target: Target value.

        Returns:
            Index of target in array if target is present, index where target should be inserted if not.

        """
        value_index = len(nums) // 2
        start_index = 0
        stop_index = len(nums) - 1
        if target > nums[-1]:
            return stop_index + 1
        elif target < nums[0]:
            return 0
        while stop_index - start_index > 1:
            if target < nums[value_index]:
                stop_index = value_index
            elif target > nums[value_index]:
                start_index = value_index
            else:
                return value_index
            value_index = start_index + (stop_index - start_index) // 2
        return start_index if nums[start_index] == target else stop_index


class TestSolution:
    solution = Solution()

    @pytest.mark.parametrize(
        "array,target,result",
        [
            ([1], 0, 0),
            ([1], 1, 0),
            ([1, 2, 3], 3, 2),
            ([1, 2, 3], 1, 0),
            ([1, 2, 3, 4], 5, 4),
            ([1, 2, 3], 0, 0),
            ([0, 2, 3, 5, 6, 7], 0, 0),
            ([1, 2, 3, 4, 5, 6, 7, 8], 3, 2),
            ([1, 3, 4, 5, 6, 7, 8], 7, 5),
            ([12, 167, 8900], 12, 0),
            ([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 8, 8),
            ([0, 1, 2, 3, 4, 6, 7, 8, 9], 5, 5),
        ]
    )
    def testSearchInsert(self, array, target, result):
        assert self.solution.searchInsert(array, target) == result
