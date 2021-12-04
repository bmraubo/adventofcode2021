import pytest
import solution


def test_read_input_file():
    test_file = "testinput.txt"

    expected_result = ["101110", "010101", "101010"]

    assert solution.read_input_file(test_file) == expected_result


def test_create_bit_list():
    test_file = "testinput.txt"

    input_list = solution.read_input_file(test_file)

    expected_result = {
        0: ["1", "0", "1"],
        1: ["0", "1", "0"],
        2: ["1", "0", "1"],
        3: ["1", "1", "0"],
        4: ["1", "0", "1"],
        5: ["0", "1", "0"],
    }

    assert solution.create_bit_columns(input_list) == expected_result


def test_rate_calculator():
    test_file = "testinput.txt"

    input_list = solution.read_input_file(test_file)

    bit_columns = solution.create_bit_columns(input_list)

    expected_gamma_result = ["1", "0", "1", "1", "1", "0"]
    expected_epsilon_result = ["0", "1", "0", "0", "0", "1"]

    assert solution.rate_calculator(bit_columns, "gamma") == expected_gamma_result
    assert solution.rate_calculator(bit_columns, "epsilon") == expected_epsilon_result


def test_convert_list_to_string():
    test_input = ["1", "0", "1", "1", "1", "0"]

    assert solution.convert_list_to_string(test_input) == "101110"


def test_convert_binary_to_integer():
    test_input = "101110"

    assert solution.convert_binary_to_integer(test_input) == 46


def test_calculate_rates():
    test_file = "testinput.txt"

    input_list = solution.read_input_file(test_file)

    bit_columns = solution.create_bit_columns(input_list)

    assert solution.calculate_gamma_rate(bit_columns) == 46
    assert solution.calculate_epsilon_rate(bit_columns) == 17


def test_calculate_power_consumption():
    test_file = "testinput.txt"

    assert solution.calculate_power_consumption(test_file) == 782
