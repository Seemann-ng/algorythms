from typing import List

import pytest


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        """Find the longest common prefix of words in list.

        Args:
            strs: List of words, longest common prefix to be found in.

        Returns:
            The longest common prefix.

        """
        strs.sort()
        prefix = ""
        for letter_index in range(len(strs[0])):
            for word_index in range(len(strs) - 1):
                if strs[word_index][letter_index] != strs[word_index + 1][letter_index]:
                    return prefix
            prefix += strs[0][letter_index]
        return prefix


class TestSolution:
    solution = Solution()

    @pytest.mark.parametrize(
        "strs,result",
        [
            (["flower", "flow", "flight"], "fl"),
            (["dog", "racecar", "car"], ""),
            (["cat", "catapult", "caterpillar"], "cat"),
        ]
    )
    def testLongestCommonPrefix(self, strs, result):
        assert self.solution.longestCommonPrefix(strs) == result
