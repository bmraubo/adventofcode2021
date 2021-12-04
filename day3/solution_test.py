import pytest
import solution

# Utility Tests


def test_read_input_file():
    test_file = "testinput.txt"

    expected_result = [
        "00100",
        "11110",
        "10110",
        "10111",
        "10101",
        "01111",
        "00111",
        "11100",
        "10000",
        "11001",
        "00010",
        "01010",
    ]

    assert solution.read_input_file(test_file) == expected_result


def test_create_bit_columns():
    test_file = "testinput.txt"

    input_list = solution.read_input_file(test_file)
    bit_rows = solution.create_bit_rows(input_list)

    expected_result = {
        0: ["0", "1", "1", "1", "1", "0", "0", "1", "1", "1", "0", "0"],
        1: ["0", "1", "0", "0", "0", "1", "0", "1", "0", "1", "0", "1"],
        2: ["1", "1", "1", "1", "1", "1", "1", "1", "0", "0", "0", "0"],
        3: ["0", "1", "1", "1", "0", "1", "1", "0", "0", "0", "1", "1"],
        4: ["0", "0", "0", "1", "1", "1", "1", "0", "0", "1", "0", "0"],
    }

    assert solution.create_bit_columns(bit_rows) == expected_result


def test_create_bit_rows():
    test_file = "testinput.txt"

    input_list = solution.read_input_file(test_file)

    expected_result = [
        ["0", "0", "1", "0", "0"],
        ["1", "1", "1", "1", "0"],
        ["1", "0", "1", "1", "0"],
        ["1", "0", "1", "1", "1"],
        ["1", "0", "1", "0", "1"],
        ["0", "1", "1", "1", "1"],
        ["0", "0", "1", "1", "1"],
        ["1", "1", "1", "0", "0"],
        ["1", "0", "0", "0", "0"],
        ["1", "1", "0", "0", "1"],
        ["0", "0", "0", "1", "0"],
        ["0", "1", "0", "1", "0"],
    ]

    assert solution.create_bit_rows(input_list) == expected_result


def test_convert_list_to_string():
    test_input = ["1", "0", "1", "1", "1", "0"]

    expected_result = "101110"

    assert solution.convert_list_to_string(test_input) == expected_result


def test_convert_string_to_list():
    test_input = "101110"

    expected_result = ["1", "0", "1", "1", "1", "0"]

    assert solution.convert_string_to_list(test_input) == expected_result


def test_convert_binary_to_integer():
    test_input = "101110"

    assert solution.convert_binary_to_integer(test_input) == 46


# Power Consumption Test


def test_calculate_power_consumption():
    test_file = "testinput.txt"

    assert solution.calculate_power_consumption(test_file) == 198


def test_power_rate_calculator():
    test_file = "testinput.txt"

    input_list = solution.read_input_file(test_file)
    bit_columns = solution.create_bit_columns(input_list)

    expected_gamma_result = ["1", "0", "1", "1", "0"]
    expected_epsilon_result = ["0", "1", "0", "0", "1"]

    assert solution.power_rate_calculator(bit_columns, "gamma") == expected_gamma_result
    assert (
        solution.power_rate_calculator(bit_columns, "epsilon")
        == expected_epsilon_result
    )


def test_calculate_rates():
    test_file = "testinput.txt"

    input_list = solution.read_input_file(test_file)

    bit_columns = solution.create_bit_columns(input_list)

    assert solution.calculate_power_rate(bit_columns, "gamma") == 22
    assert solution.calculate_power_rate(bit_columns, "epsilon") == 9


# Life Support Tests


def test_calculate_bit_criteria():
    test_file = "testinput.txt"

    input_list = solution.read_input_file(test_file)
    bit_rows = solution.create_bit_rows(input_list)
    bit_columns = solution.create_bit_columns(input_list)

    bit = 0

    expected_O2_result = "1"
    expected_CO2_result = "0"

    assert solution.calculate_bit_criteria(bit, bit_columns, "O2") == expected_O2_result
    assert (
        solution.calculate_bit_criteria(bit, bit_columns, "CO2") == expected_CO2_result
    )


def test_calculate_bit_rating():
    test_file = "testinput.txt"

    input_list = solution.read_input_file(test_file)
    bit_rows = solution.create_bit_rows(input_list)
    bit_columns = solution.create_bit_columns(bit_rows)

    expected_O2_rating = "10111"
    expected_CO2_rating = "01010"

    assert (
        solution.calculate_bit_life_support_rating(bit_rows, bit_columns, "O2")
        == expected_O2_rating
    )
    assert (
        solution.calculate_bit_life_support_rating(bit_rows, bit_columns, "CO2")
        == expected_CO2_rating
    )


def test_calculate_life_support_rating():
    test_file = "testinput.txt"

    expected = 230

    assert solution.calculate_life_support_rating(test_file)
