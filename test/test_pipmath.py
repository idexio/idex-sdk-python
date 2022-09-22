import unittest
from decimal import Decimal

from idex_sdk import pipmath as p


class TestPipmath(unittest.TestCase):
    def test_asset_units_to_decimal(self) -> None:
        self.assertEqual(p.asset_units_to_decimal(1, 3), "0.00100000")
        self.assertEqual(p.asset_units_to_decimal(999, 3), "0.99900000")
        self.assertEqual(p.asset_units_to_decimal(9999999999, 3), "9999999.99900000")

    def test_decimal_to_pip(self) -> None:
        self.assertEqual(p.decimal_to_pip("1"), 100000000)
        self.assertEqual(p.decimal_to_pip("999"), 99900000000)
        self.assertEqual(p.decimal_to_pip("0.00000001"), 1)
        self.assertEqual(p.decimal_to_pip("0.000000009"), 0)
        self.assertEqual(p.decimal_to_pip("0.000000001"), 0)
        self.assertEqual(p.decimal_to_pip("4382887.83017307"), 438288783017307)
        self.assertEqual(p.decimal_to_pip("289139.11015652"), 28913911015652)

    def test_divide_pips(self) -> None:
        self.assertEqual(p.divide_pips(1, 0), 0)
        self.assertEqual(p.divide_pips(1, 1), 100000000)
        self.assertEqual(p.divide_pips(2, 3), 66666666)
        self.assertEqual(p.divide_pips(1, 100000000), 1)
        self.assertEqual(p.divide_pips(1, 1000000000), 0)

    def test_multiply_pips(self) -> None:
        self.assertEqual(p.multiply_pips(100000000, 2), 2)
        self.assertEqual(p.multiply_pips(10000000, 2), 0)
        self.assertEqual(p.multiply_pips(10000000, 2, True), 1)

    def test_pip_to_decimal(self) -> None:
        self.assertEqual(p.pip_to_decimal(10000000), "0.10000000")

    def test_square_root_big_int(self) -> None:
        self.assertEqual(p.square_root_big_int(Decimal(0)), 0)
        self.assertEqual(p.square_root_big_int(Decimal(3)), 1)
        self.assertEqual(p.square_root_big_int(Decimal(4)), 2)
        self.assertEqual(p.square_root_big_int(Decimal(5)), 2)
        self.assertEqual(p.square_root_big_int(Decimal(200)), 14)
