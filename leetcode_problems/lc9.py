import pytest


class Solution:
    def isPalindrome(self, x: int) -> bool:
        """Tell if number is a palindrome.

        Args:
            x: Given number.

        Returns:
            True if number is a palindrome and False otherwise.

        """
        if x < 0:
            return False
        elif x < 10:
            return True
        x = str(x)
        for digit_index in range(len(x) // 2):
            if x[digit_index] != x[-digit_index - 1]:
                return False
        return True


class TestSolution:
    solution = Solution()

    @pytest.mark.parametrize(
        "x,result",
        [
            (-1, False),
            (-121, False),
            (10, False),
            (0, True),
            (5, True),
            (121, True),
            (122, False),
            (1221, True),
            (1222, False),
            (12321, True),
            (12345, False),
            (12344321, True),
            (12345678, False),
        ]
    )
    def testIsPalindrome(self, x, result):
        assert self.solution.isPalindrome(x) == result
