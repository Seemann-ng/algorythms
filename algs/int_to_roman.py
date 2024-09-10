import pytest


class Converter:
    @staticmethod
    def int_to_roman(num: int) -> str:
        """Convert number written in arabic numerals into a number written in roman numerals.

        Args:
            num: Number written in arabic numerals.

        Returns:
            Same number written in roman numerals.

        """
        roman_number = ""
        while num >= 1000:
            roman_number += "M"
            num -= 1000
        while num >= 900:
            roman_number += "CM"
            num -= 900
        while num >= 500:
            roman_number += "D"
            num -= 500
        while num >= 400:
            roman_number += "CD"
            num -= 400
        while num >= 100:
            roman_number += "C"
            num -= 100
        while num >= 90:
            roman_number += "XC"
            num -= 90
        while num >= 50:
            roman_number += "L"
            num -= 50
        while num >= 40:
            roman_number += "XL"
            num -= 40
        while num >= 10:
            roman_number += "X"
            num -= 10
        while num >= 9:
            roman_number += "IX"
            num -= 9
        while num >= 5:
            roman_number += "V"
            num -= 5
        while num >= 4:
            roman_number += "IV"
            num -= 4
        while num >= 1:
            roman_number += "I"
            num -= 1
        return roman_number


class TestConverter:
    converter = Converter()

    @pytest.mark.parametrize(
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
    def test_int_to_roman(self, num, result):
        assert self.converter.int_to_roman(num) == result
