import pytest


class Solution:
    def isValid(self, s: str) -> bool:
        """Tells if sequence of parentheses is valid.

        Args:
            s: Sequence of parentheses.

        Returns:
            True if sequence is valid and False otherwise.

        """
        stack = [""]
        for symbol_index in range(len(s)):
            if s[symbol_index] in "([{":
                stack.append(s[symbol_index])
            if s[symbol_index] in ")]}":
                if (stack[-1] != "(" and s[symbol_index] == ")") \
                        or (stack[-1] != "[" and s[symbol_index] == "]") \
                        or (stack[-1] != "{" and s[symbol_index] == "}"):
                    return False
                stack.pop()
        if len(stack) >= 2:
            return False
        return True


class TestSolution:
    solution = Solution()

    @pytest.mark.parametrize(
        "s,result",
        [
            ("()", True),
            ("()[]{}", True),
            ("(]", False),
            ("((", False),
            ("))", False),
            ("()(()){[{}]}", True),
            ("()(()){[{]}}", False),
            ("()(()){[{}]", False),
            ("()(()){[{}", False),
            ("()(()){[{", False),
        ]
    )
    def testIsValid(self, s, result):
        assert self.solution.isValid(s) == result
