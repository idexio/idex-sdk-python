EXCHANGE_DECIMALS = 8
ONE_IN_PIPS = 10**EXCHANGE_DECIMALS
MAX_64_BIT_INT = 18446744073709551615
DECIMAL_FORMAT_STR = "{:." + str(EXCHANGE_DECIMALS) + "f}"


def asset_units_to_decimal(asset_units: int, decimals: int) -> str:
    return DECIMAL_FORMAT_STR.format(asset_units / (10**decimals))


def decimal_to_pip(decimal: str) -> int:
    return int(float(decimal) * ONE_IN_PIPS)


def divide_pips(value_in_pips: int, divisor_in_pips: int) -> int:
    if divisor_in_pips <= 0:
        return 0
    return int((value_in_pips * ONE_IN_PIPS) / divisor_in_pips)


def multiply_pips(pip_value_1: int, pip_value_2: int, round_up: bool = False) -> int:
    pip_values_product = pip_value_1 * pip_value_2
    if round_up and pip_values_product % ONE_IN_PIPS > 0:
        return int(1 + pip_values_product / ONE_IN_PIPS)
    return int(pip_values_product / ONE_IN_PIPS)


def pip_to_decimal(pips: int) -> str:
    return asset_units_to_decimal(pips, EXCHANGE_DECIMALS)


def square_root_big_int(value: int) -> int:
    if value < 0:
        raise ValueError("Square root of negative numbers is not supported")
    elif value == 0:
        return value
    elif value <= 3:
        return 1
    z = value
    x = int(value / 2) + 1
    while x < z:
        z = x
        x = int((int(value / x) + x) / 2)
    return z
