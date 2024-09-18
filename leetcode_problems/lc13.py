import pytest


class Solution:
    @staticmethod
    def romanToInt(s: str) -> int:
        """Convert number written in roman numerals into a number written in arabic numerals.

        Args:
            s: Number written in roman numerals.

        Returns:
            Same number written in arabic numerals.

        """
        number, symbol_index = 0, 0
        while symbol_index < len(s):
            if s[symbol_index] == "M":
                number += 1000
                symbol_index += 1
                continue
            if s[symbol_index] == "D":
                number += 500
                symbol_index += 1
                continue
            if s[symbol_index] == "C":
                if symbol_index < len(s) - 1 and s[symbol_index + 1] == "M":
                    number += 900
                    symbol_index += 2
                    continue
                if symbol_index < len(s) - 1 and s[symbol_index + 1] == "D":
                    number += 400
                    symbol_index += 2
                    continue
                number += 100
                symbol_index += 1
                continue
            if s[symbol_index] == "L":
                number += 50
                symbol_index += 1
                continue
            if s[symbol_index] == "X":
                if symbol_index < len(s) - 1 and s[symbol_index + 1] == "C":
                    number += 90
                    symbol_index += 2
                    continue
                if symbol_index < len(s) - 1 and s[symbol_index + 1] == "L":
                    number += 40
                    symbol_index += 2
                    continue
                number += 10
                symbol_index += 1
                continue
            if s[symbol_index] == "V":
                number += 5
                symbol_index += 1
                continue
            if s[symbol_index] == "I":
                if symbol_index < len(s) - 1 and s[symbol_index + 1] == "X":
                    number += 9
                    symbol_index += 2
                    continue
                if symbol_index < len(s) - 1 and s[symbol_index + 1] == "V":
                    number += 4
                    symbol_index += 2
                    continue
                number += 1
                symbol_index += 1
                continue
        return number


class TestSolution:
    solution = Solution()

    @pytest.mark.parametrize(
        "s,result",
        [
            ("I", 1),
            ("III", 3),
            ("LVIII", 58),
            ("MCMXCIV", 1994),
            ("IV", 4),
            ("V", 5),
            ("VIII", 8),
            ("IX", 9),
            ("X", 10),
            ("XIV", 14),
            ("XXIX", 29),
            ("XLIX", 49),
            ("CXIV", 114),
            ("CCCXLIX", 349),
            ("CDLIV", 454),
            ("CMLXXXIX", 989),
            ("CMXCIX", 999),
            ("M", 1000),
            ("MCDXLIX", 1449),
            ("MCMLXXXIV", 1984),
            ("MCMXCIX", 1999),
            ("MCMXCIX", 1999),
            ("MMMCMXCIX", 3999),

        ]
    )
    def testRomanToInt(self, s, result):
        assert self.solution.romanToInt(s) == result
