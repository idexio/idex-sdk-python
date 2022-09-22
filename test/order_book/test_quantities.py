import unittest
from decimal import ROUND_DOWN, ROUND_HALF_UP, ROUND_UP
from typing import List

from idex_sdk.idex_types.order_book import L2OrderBook, OrderBookLevelL2
from idex_sdk.order_book import quantities as q
from idex_sdk.pipmath import ONE_IN_PIPS


class TestOrderBookQuantities(unittest.TestCase):
    maxDiff = None

    def test_adjust_price_to_tick_size(self) -> None:
        self.assertEqual(q.adjust_price_to_tick_size(1000000005, 1), 1000000005)
        self.assertEqual(q.adjust_price_to_tick_size(1000000005, 10), 1000000010)
        self.assertEqual(q.adjust_price_to_tick_size(1000000005, 100), 1000000000)

        self.assertEqual(
            q.adjust_price_to_tick_size(1000000005, 1, q.BIDS_TICK_ROUNDING_MODE), 1000000005
        )
        self.assertEqual(
            q.adjust_price_to_tick_size(1000000005, 10, q.BIDS_TICK_ROUNDING_MODE), 1000000000
        )
        self.assertEqual(
            q.adjust_price_to_tick_size(1000000005, 100, q.BIDS_TICK_ROUNDING_MODE), 1000000000
        )
        self.assertEqual(
            q.adjust_price_to_tick_size(123456789, 1, q.BIDS_TICK_ROUNDING_MODE), 123456789
        )
        self.assertEqual(
            q.adjust_price_to_tick_size(123456789, 10, q.BIDS_TICK_ROUNDING_MODE), 123456780
        )
        self.assertEqual(
            q.adjust_price_to_tick_size(123456789, 100, q.BIDS_TICK_ROUNDING_MODE), 123456700
        )
        self.assertEqual(
            q.adjust_price_to_tick_size(987654321, 1, q.BIDS_TICK_ROUNDING_MODE), 987654321
        )
        self.assertEqual(
            q.adjust_price_to_tick_size(987654321, 10, q.BIDS_TICK_ROUNDING_MODE), 987654320
        )
        self.assertEqual(
            q.adjust_price_to_tick_size(987654321, 100, q.BIDS_TICK_ROUNDING_MODE), 987654300
        )

        self.assertEqual(
            q.adjust_price_to_tick_size(1000000005, 1, q.ASKS_TICK_ROUNDING_MODE), 1000000005
        )
        self.assertEqual(
            q.adjust_price_to_tick_size(1000000005, 10, q.ASKS_TICK_ROUNDING_MODE), 1000000010
        )
        self.assertEqual(
            q.adjust_price_to_tick_size(1000000005, 100, q.ASKS_TICK_ROUNDING_MODE), 1000000100
        )
        self.assertEqual(
            q.adjust_price_to_tick_size(123456789, 1, q.ASKS_TICK_ROUNDING_MODE), 123456789
        )
        self.assertEqual(
            q.adjust_price_to_tick_size(123456789, 10, q.ASKS_TICK_ROUNDING_MODE), 123456790
        )
        self.assertEqual(
            q.adjust_price_to_tick_size(123456789, 100, q.ASKS_TICK_ROUNDING_MODE), 123456800
        )
        self.assertEqual(
            q.adjust_price_to_tick_size(987654321, 1, q.ASKS_TICK_ROUNDING_MODE), 987654321
        )
        self.assertEqual(
            q.adjust_price_to_tick_size(987654321, 10, q.ASKS_TICK_ROUNDING_MODE), 987654330
        )
        self.assertEqual(
            q.adjust_price_to_tick_size(987654321, 100, q.ASKS_TICK_ROUNDING_MODE), 987654400
        )

    def test_calculate_gross_quote_quantity(self) -> None:
        self.assertEqual(
            q.calculate_gross_quote_quantity(
                int(1000 * ONE_IN_PIPS),
                int(2000 * ONE_IN_PIPS),
                int(3 * ONE_IN_PIPS),
                10,
                15,
            ),
            44948982144,
        )
        self.assertEqual(
            q.calculate_gross_quote_quantity(
                int(5000 * ONE_IN_PIPS),
                int(6000 * ONE_IN_PIPS),
                int(2 * ONE_IN_PIPS),
                100,
                150,
            ),
            174596974786,
        )

    def test_calculate_gross_base_value_of_buy_quantities(self) -> None:
        self.assertEqual(
            q.calculate_gross_base_value_of_buy_quantities(
                int(1000 * ONE_IN_PIPS), int(2000 * ONE_IN_PIPS), 100
            ),
            50,
        )
        self.assertEqual(
            q.calculate_gross_base_value_of_buy_quantities(
                int(5000 * ONE_IN_PIPS), int(6000 * ONE_IN_PIPS), 123
            ),
            103,
        )
        self.assertEqual(
            q.calculate_gross_base_value_of_buy_quantities(
                449805511517087, 28941050006305, 1970218377
            ),
            30619302271,
        )

    def test_quantities_available_from_pool_at_ask_price(self) -> None:
        self.assertEqual(
            q.quantities_available_from_pool_at_ask_price(
                int(5000 * ONE_IN_PIPS),
                int(6000 * ONE_IN_PIPS),
                int(2 * ONE_IN_PIPS),
                int(10),
                int(15),
            ),
            {"gross_base": 112701680657, "gross_quote": 174596699795},
        )
        self.assertEqual(
            q.quantities_available_from_pool_at_ask_price(
                int(1100 * ONE_IN_PIPS),
                int(700 * ONE_IN_PIPS),
                int(2 * ONE_IN_PIPS),
                12,
                13,
            ),
            {"gross_base": 47951636774, "gross_quote": 54096746467},
        )

    def test_calculate_gross_base_quantity(self) -> None:
        self.assertEqual(
            q.calculate_gross_base_quantity(
                int(5000 * ONE_IN_PIPS),
                int(6000 * ONE_IN_PIPS),
                int(1 * ONE_IN_PIPS),
                10,
                15,
            ),
            47722565856,
        )
        self.assertEqual(
            q.calculate_gross_base_quantity(
                int(1100 * ONE_IN_PIPS),
                int(7000 * ONE_IN_PIPS),
                int(2 * ONE_IN_PIPS),
                12,
                13,
            ),
            86214184653,
        )

    def test_quantities_available_from_pool_at_bid_price(self) -> None:
        self.assertEqual(
            q.quantities_available_from_pool_at_bid_price(
                int(5000 * ONE_IN_PIPS),
                int(6000 * ONE_IN_PIPS),
                int(1 * ONE_IN_PIPS),
                10,
                15,
            ),
            {"gross_base": 47722565856, "gross_quote": 52277450846},
        )
        self.assertEqual(
            q.quantities_available_from_pool_at_bid_price(
                int(1100 * ONE_IN_PIPS),
                int(7000 * ONE_IN_PIPS),
                int(2 * ONE_IN_PIPS),
                12,
                13,
            ),
            {"gross_base": 86214184653, "gross_quote": 307571694493},
        )

    def test_calculate_synthetic_price_levels(self) -> None:
        self.assertEqual(
            q.calculate_synthetic_price_levels(
                int(5000 * ONE_IN_PIPS),
                int(6000 * ONE_IN_PIPS),
                3,
                100,
                10,
                15,
                1,
            ),
            {
                "asks": [
                    {"price": 120120000, "size": 249812700, "num_orders": 0, "type": "pool"},
                    {"price": 120240000, "size": 249438636, "num_orders": 0, "type": "pool"},
                    {"price": 120360000, "size": 249065503, "num_orders": 0, "type": "pool"},
                ],
                "bids": [
                    {"price": 119880000, "size": 250187700, "num_orders": 0, "type": "pool"},
                    {"price": 119760000, "size": 250563639, "num_orders": 0, "type": "pool"},
                    {"price": 119640000, "size": 250940522, "num_orders": 0, "type": "pool"},
                ],
                "pool": {
                    "base_reserve_quantity": 500000000000,
                    "quote_reserve_quantity": 600000000000,
                },
            },
        )

    def test_recalculate_hybrid_level_amounts(self) -> None:
        orderbook: L2OrderBook = {
            "sequence": 0,
            "asks": [
                {"price": 120120000, "size": 249812700, "num_orders": 0, "type": "limit"},
                {"price": 120240000, "size": 249438636, "num_orders": 0, "type": "limit"},
                {"price": 120360000, "size": 249065503, "num_orders": 0, "type": "limit"},
            ],
            "bids": [
                {"price": 119880000, "size": 250187700, "num_orders": 0, "type": "limit"},
                {"price": 119760000, "size": 250563639, "num_orders": 0, "type": "limit"},
                {"price": 119640000, "size": 250940522, "num_orders": 0, "type": "limit"},
            ],
            "pool": {
                "base_reserve_quantity": 500000000000,
                "quote_reserve_quantity": 600000000000,
            },
        }
        orderbook = q.recalculate_hybrid_level_amounts(orderbook, 10, 15)
        self.assertEqual(
            orderbook,
            {
                "sequence": 0,
                "asks": [
                    {"price": 120120000, "size": 499625400, "num_orders": 0, "type": "limit"},
                    {"price": 120240000, "size": 498877272, "num_orders": 0, "type": "limit"},
                    {"price": 120360000, "size": 498131006, "num_orders": 0, "type": "limit"},
                ],
                "bids": [
                    {"price": 119880000, "size": 500375400, "num_orders": 0, "type": "limit"},
                    {"price": 119760000, "size": 501127278, "num_orders": 0, "type": "limit"},
                    {"price": 119640000, "size": 501881044, "num_orders": 0, "type": "limit"},
                ],
                "pool": {
                    "base_reserve_quantity": 500000000000,
                    "quote_reserve_quantity": 600000000000,
                },
            },
        )

        orderbook = {
            "sequence": 0,
            "asks": [
                {"price": 120120000, "size": 249812700, "num_orders": 0, "type": "limit"},
                {"price": 120240000, "size": 249438636, "num_orders": 0, "type": "limit"},
                {"price": 120360000, "size": 249065503, "num_orders": 0, "type": "pool"},
            ],
            "bids": [
                {"price": 119880000, "size": 250187700, "num_orders": 0, "type": "limit"},
                {"price": 119760000, "size": 250563639, "num_orders": 0, "type": "limit"},
                {"price": 119640000, "size": 250940522, "num_orders": 0, "type": "pool"},
            ],
            "pool": {
                "base_reserve_quantity": 500000000000,
                "quote_reserve_quantity": 600000000000,
            },
        }
        orderbook = q.recalculate_hybrid_level_amounts(orderbook, 10, 15)
        self.assertEqual(
            orderbook,
            {
                "sequence": 0,
                "asks": [
                    {"price": 120120000, "size": 499625400, "num_orders": 0, "type": "limit"},
                    {"price": 120240000, "size": 498877272, "num_orders": 0, "type": "limit"},
                    {"price": 120360000, "size": 249065503, "num_orders": 0, "type": "pool"},
                ],
                "bids": [
                    {"price": 119880000, "size": 500375400, "num_orders": 0, "type": "limit"},
                    {"price": 119760000, "size": 501127278, "num_orders": 0, "type": "limit"},
                    {"price": 119640000, "size": 250940522, "num_orders": 0, "type": "pool"},
                ],
                "pool": {
                    "base_reserve_quantity": 500000000000,
                    "quote_reserve_quantity": 600000000000,
                },
            },
        )

    def test_calculate_base_quantity_out(self) -> None:
        self.assertEqual(
            q.calculate_base_quantity_out(
                int(5000 * ONE_IN_PIPS),
                int(6000 * ONE_IN_PIPS),
                int(200 * ONE_IN_PIPS),
                10,
                15,
            ),
            16129028355,
        )

    def test_calculate_quote_quantity_out(self) -> None:
        self.assertEqual(
            q.calculate_quote_quantity_out(
                int(5000 * ONE_IN_PIPS),
                int(6000 * ONE_IN_PIPS),
                int(200 * ONE_IN_PIPS),
                10,
                15,
            ),
            23076917529,
        )

    def test_l1_or_l2_best_available_prices(self) -> None:
        self.assertEqual(
            q.l1_or_l2_best_available_prices(
                {
                    "base_reserve_quantity": int(5000 * ONE_IN_PIPS),
                    "quote_reserve_quantity": int(6000 * ONE_IN_PIPS),
                },
                10,
                15,
                int(200 * ONE_IN_PIPS),
                int(250 * ONE_IN_PIPS),
                1,
            ),
            {"buy_price": 130208331, "sell_price": 110946747},
        )

    def test_l1_l2_order_books_with_minimum_taker(self) -> None:
        orderbook: L2OrderBook = {
            "sequence": 0,
            "asks": [
                {"price": 120120000, "size": 249812700, "num_orders": 0, "type": "limit"},
                {"price": 120240000, "size": 249438636, "num_orders": 0, "type": "limit"},
                {"price": 120360000, "size": 249065503, "num_orders": 0, "type": "limit"},
            ],
            "bids": [
                {"price": 119880000, "size": 250187700, "num_orders": 0, "type": "limit"},
                {"price": 119760000, "size": 250563639, "num_orders": 0, "type": "limit"},
                {"price": 119640000, "size": 250940522, "num_orders": 0, "type": "limit"},
            ],
            "pool": {
                "base_reserve_quantity": 500000000000,
                "quote_reserve_quantity": 600000000000,
            },
        }
        result = q.l1_l2_order_books_with_minimum_taker(
            orderbook,
            10,
            15,
            int(200 * ONE_IN_PIPS),
            1,
        )

        self.assertEqual(
            result,
            {
                "l1": {
                    "sequence": 0,
                    "asks": {"price": 120120000, "size": 249812700, "num_orders": 0},
                    "bids": {"price": 119880000, "size": 250187700, "num_orders": 0},
                    "pool": {
                        "base_reserve_quantity": 500000000000,
                        "quote_reserve_quantity": 600000000000,
                    },
                },
                "l2": {
                    "sequence": 0,
                    "asks": [
                        {"price": 120120000, "size": 249812700, "num_orders": 0, "type": "limit"},
                        {"price": 120240000, "size": 249438636, "num_orders": 0, "type": "limit"},
                        {"price": 120360000, "size": 249065503, "num_orders": 0, "type": "limit"},
                    ],
                    "bids": [
                        {"price": 119880000, "size": 250187700, "num_orders": 0, "type": "limit"},
                        {"price": 119760000, "size": 250563639, "num_orders": 0, "type": "limit"},
                        {"price": 119640000, "size": 250940522, "num_orders": 0, "type": "limit"},
                    ],
                    "pool": {
                        "base_reserve_quantity": 500000000000,
                        "quote_reserve_quantity": 600000000000,
                    },
                },
            },
        )

    def test_aggregate_l2_order_book_at_tick_size(self) -> None:
        input_book: L2OrderBook = {
            "sequence": 1130790,
            "asks": [
                {"price": 6913000, "size": 521801431648, "num_orders": 1, "type": "limit"},
                {"price": 7231000, "size": 25519896132, "num_orders": 1, "type": "limit"},
                {"price": 7950000, "size": 207668294256, "num_orders": 1, "type": "limit"},
                {"price": 8200000, "size": 113300000000, "num_orders": 1, "type": "limit"},
                {"price": 8350000, "size": 66000000000, "num_orders": 1, "type": "limit"},
                {"price": 9000000, "size": 213865083350, "num_orders": 1, "type": "limit"},
                {"price": 9300000, "size": 187622858589, "num_orders": 1, "type": "limit"},
                {"price": 9400000, "size": 136857165273, "num_orders": 1, "type": "limit"},
                {"price": 9600000, "size": 320797627929, "num_orders": 1, "type": "limit"},
                {"price": 9758000, "size": 5969600000000, "num_orders": 1, "type": "limit"},
                {"price": 9975000, "size": 202396588079, "num_orders": 1, "type": "limit"},
                {"price": 10000000, "size": 82391006332, "num_orders": 2, "type": "limit"},
                {"price": 10400000, "size": 320797627929, "num_orders": 1, "type": "limit"},
                {"price": 10900000, "size": 199999999858, "num_orders": 1, "type": "limit"},
                {"price": 11000000, "size": 500000000000, "num_orders": 1, "type": "limit"},
                {"price": 11400000, "size": 299999999673, "num_orders": 1, "type": "limit"},
                {"price": 11500000, "size": 200000000000, "num_orders": 1, "type": "limit"},
                {"price": 11613000, "size": 955692792178, "num_orders": 1, "type": "limit"},
                {"price": 11980000, "size": 200000000000, "num_orders": 1, "type": "limit"},
                {"price": 12000000, "size": 651946634416, "num_orders": 4, "type": "limit"},
                {"price": 12900000, "size": 200000000000, "num_orders": 1, "type": "limit"},
                {"price": 13000000, "size": 500000000000, "num_orders": 1, "type": "limit"},
                {"price": 13300000, "size": 40000000000, "num_orders": 1, "type": "limit"},
                {"price": 13900000, "size": 200000000000, "num_orders": 1, "type": "limit"},
                {"price": 14000000, "size": 500000000000, "num_orders": 1, "type": "limit"},
            ],
            "bids": [
                {"price": 6500000, "size": 43416670784, "num_orders": 1, "type": "limit"},
                {"price": 6250000, "size": 125000000000, "num_orders": 1, "type": "limit"},
                {"price": 6137000, "size": 44936452305, "num_orders": 1, "type": "limit"},
                {"price": 6010000, "size": 64034347038, "num_orders": 1, "type": "limit"},
                {"price": 5700000, "size": 106114304122, "num_orders": 1, "type": "limit"},
                {"price": 5000000, "size": 1500000000000, "num_orders": 1, "type": "limit"},
                {"price": 4501000, "size": 928895228015, "num_orders": 1, "type": "limit"},
                {"price": 4490000, "size": 291024042249, "num_orders": 1, "type": "limit"},
            ],
            "pool": {
                "base_reserve_quantity": 438288783017306,
                "quote_reserve_quantity": 28913911015651,
            },
        }

        correct_result = {
            "asks": [
                {"price": 6913000, "size": 521801431648, "num_orders": 1, "type": "limit"},
                {"price": 7231000, "size": 25519896132, "num_orders": 1, "type": "limit"},
                {"price": 7950000, "size": 207668294256, "num_orders": 1, "type": "limit"},
                {"price": 8200000, "size": 113300000000, "num_orders": 1, "type": "limit"},
                {"price": 8350000, "size": 66000000000, "num_orders": 1, "type": "limit"},
                {"price": 9000000, "size": 213865083350, "num_orders": 1, "type": "limit"},
                {"price": 9300000, "size": 187622858589, "num_orders": 1, "type": "limit"},
                {"price": 9400000, "size": 136857165273, "num_orders": 1, "type": "limit"},
                {"price": 9600000, "size": 320797627929, "num_orders": 1, "type": "limit"},
                {"price": 9758000, "size": 5969600000000, "num_orders": 1, "type": "limit"},
                {"price": 9975000, "size": 202396588079, "num_orders": 1, "type": "limit"},
                {"price": 10000000, "size": 82391006332, "num_orders": 2, "type": "limit"},
                {"price": 10400000, "size": 320797627929, "num_orders": 1, "type": "limit"},
                {"price": 10900000, "size": 199999999858, "num_orders": 1, "type": "limit"},
                {"price": 11000000, "size": 500000000000, "num_orders": 1, "type": "limit"},
                {"price": 11400000, "size": 299999999673, "num_orders": 1, "type": "limit"},
                {"price": 11500000, "size": 200000000000, "num_orders": 1, "type": "limit"},
                {"price": 11613000, "size": 955692792178, "num_orders": 1, "type": "limit"},
                {"price": 11980000, "size": 200000000000, "num_orders": 1, "type": "limit"},
                {"price": 12000000, "size": 651946634416, "num_orders": 4, "type": "limit"},
                {"price": 12900000, "size": 200000000000, "num_orders": 1, "type": "limit"},
                {"price": 13000000, "size": 500000000000, "num_orders": 1, "type": "limit"},
                {"price": 13300000, "size": 40000000000, "num_orders": 1, "type": "limit"},
                {"price": 13900000, "size": 200000000000, "num_orders": 1, "type": "limit"},
                {"price": 14000000, "size": 500000000000, "num_orders": 1, "type": "limit"},
            ],
            "bids": [
                {"price": 6500000, "size": 43416670784, "num_orders": 1, "type": "limit"},
                {"price": 6250000, "size": 125000000000, "num_orders": 1, "type": "limit"},
                {"price": 6137000, "size": 44936452305, "num_orders": 1, "type": "limit"},
                {"price": 6010000, "size": 64034347038, "num_orders": 1, "type": "limit"},
                {"price": 5700000, "size": 106114304122, "num_orders": 1, "type": "limit"},
                {"price": 5000000, "size": 1500000000000, "num_orders": 1, "type": "limit"},
                {"price": 4501000, "size": 928895228015, "num_orders": 1, "type": "limit"},
                {"price": 4490000, "size": 291024042249, "num_orders": 1, "type": "limit"},
            ],
            "sequence": 1130790,
            "pool": {
                "base_reserve_quantity": 438288783017306,
                "quote_reserve_quantity": 28913911015651,
            },
        }
        result = q.aggregate_l2_order_book_at_tick_size(input_book, 1000)
        self.assertEqual(result, correct_result)

    def test_sort_and_merge_levels_unadjusted(self) -> None:
        limit_order_levels: List[OrderBookLevelL2] = [
            {"price": 6913000, "size": 521801431648, "num_orders": 1, "type": "limit"},
            {"price": 7231000, "size": 25519896132, "num_orders": 1, "type": "limit"},
        ]
        synthetic_levels: List[OrderBookLevelL2] = [
            {"price": 6905000, "size": 217625260812, "num_orders": 0, "type": "pool"},
            {"price": 6912000, "size": 217294259804, "num_orders": 0, "type": "pool"},
            {"price": 6913000, "size": 217101431648, "num_orders": 0, "type": "pool"},
            {"price": 6919000, "size": 216964096782, "num_orders": 0, "type": "pool"},
            {"price": 6926000, "size": 216634768928, "num_orders": 0, "type": "pool"},
            {"price": 7220000, "size": 203519707432, "num_orders": 0, "type": "pool"},
            {"price": 7227000, "size": 203223662176, "num_orders": 0, "type": "pool"},
            {"price": 7231000, "size": 203028333849, "num_orders": 0, "type": "pool"},
            {"price": 7234000, "size": 202928333849, "num_orders": 0, "type": "pool"},
            {"price": 7241000, "size": 202633720022, "num_orders": 0, "type": "pool"},
        ]
        is_before = lambda a, b: a["price"] <= b["price"]
        result = q.sort_and_merge_levels_unadjusted(limit_order_levels, synthetic_levels, is_before)
        self.assertEqual(
            result,
            [
                {"price": 6905000, "size": 217625260812, "num_orders": 0, "type": "pool"},
                {"price": 6912000, "size": 217294259804, "num_orders": 0, "type": "pool"},
                {"price": 6913000, "size": 521801431648, "num_orders": 1, "type": "limit"},
                {"price": 6919000, "size": 216964096782, "num_orders": 0, "type": "pool"},
                {"price": 6926000, "size": 216634768928, "num_orders": 0, "type": "pool"},
                {"price": 7220000, "size": 203519707432, "num_orders": 0, "type": "pool"},
                {"price": 7227000, "size": 203223662176, "num_orders": 0, "type": "pool"},
                {"price": 7231000, "size": 25519896132, "num_orders": 1, "type": "limit"},
                {"price": 7234000, "size": 202928333849, "num_orders": 0, "type": "pool"},
                {"price": 7241000, "size": 202633720022, "num_orders": 0, "type": "pool"},
            ],
        )


if __name__ == "__main__":
    unittest.main()
