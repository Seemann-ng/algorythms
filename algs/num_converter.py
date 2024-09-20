import pytest


class Converter:
    @staticmethod
    def int_to_roman(num: int) -> str | None:
        """Convert number written in arabic numerals into a number written in roman numerals.

        Args:
            num: Number written in arabic numerals.

        Returns:
            Same number written in roman numerals.

        """
        if num <= 0:
            return "Number must be greater than zero."
        roman_number = ""
        numeral_values = {
            "M": 1000,
            "CM": 900,
            "D": 500,
            "CD": 400,
            "C": 100,
            "XC": 90,
            "L": 50,
            "XL": 40,
            "X": 10,
            "IX": 9,
            "V": 5,
            "IV": 4,
            "I": 1
        }
        for symbol in numeral_values:
            while num >= numeral_values[symbol]:
                roman_number += symbol
                num -= numeral_values[symbol]
        return roman_number

    @staticmethod
    def roman_to_int(roman_num: str) -> int:
        """Convert number written in roman numerals into a number written in arabic numerals.

        Args:
            roman_num: Number written in roman numerals.

        Returns:
            Same number written in arabic numerals.

        """
        number, symbol_index = 0, 0
        while symbol_index < len(roman_num):
            if roman_num[symbol_index] == "M":
                number += 1000
                symbol_index += 1
                continue
            if roman_num[symbol_index] == "D":
                number += 500
                symbol_index += 1
                continue
            if roman_num[symbol_index] == "C":
                if symbol_index < len(roman_num) - 1 and roman_num[symbol_index + 1] == "M":
                    number += 900
                    symbol_index += 2
                    continue
                if symbol_index < len(roman_num) - 1 and roman_num[symbol_index + 1] == "D":
                    number += 400
                    symbol_index += 2
                    continue
                number += 100
                symbol_index += 1
                continue
            if roman_num[symbol_index] == "L":
                number += 50
                symbol_index += 1
                continue
            if roman_num[symbol_index] == "X":
                if symbol_index < len(roman_num) - 1 and roman_num[symbol_index + 1] == "C":
                    number += 90
                    symbol_index += 2
                    continue
                if symbol_index < len(roman_num) - 1 and roman_num[symbol_index + 1] == "L":
                    number += 40
                    symbol_index += 2
                    continue
                number += 10
                symbol_index += 1
                continue
            if roman_num[symbol_index] == "V":
                number += 5
                symbol_index += 1
                continue
            if roman_num[symbol_index] == "I":
                if symbol_index < len(roman_num) - 1 and roman_num[symbol_index + 1] == "X":
                    number += 9
                    symbol_index += 2
                    continue
                if symbol_index < len(roman_num) - 1 and roman_num[symbol_index + 1] == "V":
                    number += 4
                    symbol_index += 2
                    continue
                number += 1
                symbol_index += 1
                continue
        return number


Converter.int_to_roman(241)
class TestConverter:
    converter = Converter()
    params = pytest.mark.parametrize(
        "result,num",
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

    @params
    def test_int_to_roman(self, num, result):
        assert self.converter.int_to_roman(num) == result

    @params
    def test_roman_to_int(self, result, num):
        assert self.converter.roman_to_int(result) == num
