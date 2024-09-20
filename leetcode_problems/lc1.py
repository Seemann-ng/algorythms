from typing import List

import pytest


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """Find indices of two values that in summary are equal to target value.

        Args:
            nums: Array of numbers to find.
            target: Summary value.

        Returns:
            Indices of values being found.

        """
        differences = set()
        for value in nums:
            differences.add(target - value)
        value1, value2 = 0, 0
        arg = False
        for value in nums:
            if value in differences:
                if value == target - value and not arg:
                    arg = True
                    continue
                value1 = value
                value2 = target - value
                break
        value1_index = nums.index(value1)
        nums[value1_index] = None
        value2_index = nums.index(value2)
        return [value1_index, value2_index]


class TestSolution:
    solution = Solution()

    @pytest.mark.parametrize(
        "nums,target,result",
        [
            ([3, 2, 4], 6, [1, 2]),
            ([3, 3], 6, [0, 1]),
            ([-5, 3, 16], 11, [0, 2]),
        ]
    )
    def testTwoSum(self, nums, target, result):
        assert self.solution.twoSum(nums, target) == result
