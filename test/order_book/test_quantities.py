from decimal import ROUND_DOWN, ROUND_HALF_UP, ROUND_UP
import unittest

from idex_sdk_python.idex_types.order_book import L2OrderBook
from idex_sdk_python.order_book import quantities as q
from idex_sdk_python.pipmath import ONE_IN_PIPS


class TestOrderBookQuantities(unittest.TestCase):
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
                1000 * ONE_IN_PIPS,
                2000 * ONE_IN_PIPS,
                3 * ONE_IN_PIPS,
                10,
                15,
            ),
            44948982144,
        )
        self.assertEqual(
            q.calculate_gross_quote_quantity(
                5000 * ONE_IN_PIPS,
                6000 * ONE_IN_PIPS,
                2 * ONE_IN_PIPS,
                100,
                150,
            ),
            174596974786,
        )

    def test_calculate_gross_base_value_of_buy_quantities(self) -> None:
        self.assertEqual(
            q.calculate_gross_base_value_of_buy_quantities(
                1000 * ONE_IN_PIPS, 2000 * ONE_IN_PIPS, 100
            ),
            50,
        )
        self.assertEqual(
            q.calculate_gross_base_value_of_buy_quantities(
                5000 * ONE_IN_PIPS, 6000 * ONE_IN_PIPS, 123
            ),
            103,
        )

    def test_quantities_available_from_pool_at_ask_price(self) -> None:
        self.assertEqual(
            q.quantities_available_from_pool_at_ask_price(
                5000 * ONE_IN_PIPS,
                6000 * ONE_IN_PIPS,
                2 * ONE_IN_PIPS,
                10,
                15,
            ),
            {"gross_base": 112701680657, "gross_quote": 174596699795},
        )
        self.assertEqual(
            q.quantities_available_from_pool_at_ask_price(
                1100 * ONE_IN_PIPS,
                700 * ONE_IN_PIPS,
                2 * ONE_IN_PIPS,
                12,
                13,
            ),
            {"gross_base": 47951636774, "gross_quote": 54096746467},
        )

    def test_calculate_gross_base_quantity(self) -> None:
        self.assertEqual(
            q.calculate_gross_base_quantity(
                5000 * ONE_IN_PIPS,
                6000 * ONE_IN_PIPS,
                1 * ONE_IN_PIPS,
                10,
                15,
            ),
            47722565856,
        )
        self.assertEqual(
            q.calculate_gross_base_quantity(
                1100 * ONE_IN_PIPS,
                7000 * ONE_IN_PIPS,
                2 * ONE_IN_PIPS,
                12,
                13,
            ),
            86214184653,
        )

    def test_quantities_available_from_pool_at_bid_price(self) -> None:
        self.assertEqual(
            q.quantities_available_from_pool_at_bid_price(
                5000 * ONE_IN_PIPS,
                6000 * ONE_IN_PIPS,
                1 * ONE_IN_PIPS,
                10,
                15,
            ),
            {"gross_base": 47722565856, "gross_quote": 52277450846},
        )
        self.assertEqual(
            q.quantities_available_from_pool_at_bid_price(
                1100 * ONE_IN_PIPS,
                7000 * ONE_IN_PIPS,
                2 * ONE_IN_PIPS,
                12,
                13,
            ),
            {"gross_base": 86214184653, "gross_quote": 307571694493},
        )

    def test_calculate_synthetic_price_levels(self) -> None:
        self.assertEqual(
            q.calculate_synthetic_price_levels(
                5000 * ONE_IN_PIPS,
                6000 * ONE_IN_PIPS,
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
                5000 * ONE_IN_PIPS,
                6000 * ONE_IN_PIPS,
                200 * ONE_IN_PIPS,
                10,
                15,
            ),
            16129028355,
        )

    def test_calculate_quote_quantity_out(self) -> None:
        self.assertEqual(
            q.calculate_quote_quantity_out(
                5000 * ONE_IN_PIPS,
                6000 * ONE_IN_PIPS,
                200 * ONE_IN_PIPS,
                10,
                15,
            ),
            23076917529,
        )

    def test_l1_or_l2_best_available_prices(self) -> None:
        self.assertEqual(
            q.l1_or_l2_best_available_prices(
                {
                    "base_reserve_quantity": 5000 * ONE_IN_PIPS,
                    "quote_reserve_quantity": 6000 * ONE_IN_PIPS,
                },
                10,
                15,
                200 * ONE_IN_PIPS,
                250 * ONE_IN_PIPS,
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
            200 * ONE_IN_PIPS,
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

    def test_sort_and_merge_levels_unadjusted(self) -> None:
        pass

    def test_aggregate_l2_order_book_at_tick_size(self) -> None:
        pass
