import pytest
import solution


def test_read_input_file():
    test_file = "testinput.txt"

    expected_result = ["101110", "010101", "101010"]

    assert solution.read_input_file(test_file) == expected_result


def test_create_bit_columns():
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


def test_create_bit_rows():
    test_file = "testinput.txt"

    input_list = solution.read_input_file(test_file)

    expected_result = {
        0: ["1", "0", "1", "1", "1", "0"],
        1: ["0", "1", "0", "1", "0", "1"],
        2: ["1", "0", "1", "0", "1", "0"],
    }

    assert solution.create_bit_rows(input_list) == expected_result


def test_calculate_bit_criteria():
    test_file = "testinput.txt"

    input_list = solution.read_input_file(test_file)
    bit_rows = solution.create_bit_rows(input_list)
    bit_columns = solution.create_bit_columns(input_list)

    expected_O2_result = ["1", "0", "1", "1", "1", "0"]
    expected_CO2_result = ["0", "1", "0", "0", "0", "1"]

    assert (
        solution.calculate_bit_criteria(bit_rows[0], bit_columns, "O2")
        == expected_O2_result
    )
    assert (
        solution.calculate_bit_criteria(bit_rows[0], bit_columns, "CO2")
        == expected_CO2_result
    )


def test_power_rate_calculator():
    test_file = "testinput.txt"

    input_list = solution.read_input_file(test_file)
    bit_columns = solution.create_bit_columns(input_list)

    expected_gamma_result = ["1", "0", "1", "1", "1", "0"]
    expected_epsilon_result = ["0", "1", "0", "0", "0", "1"]

    assert solution.power_rate_calculator(bit_columns, "gamma") == expected_gamma_result
    assert (
        solution.power_rate_calculator(bit_columns, "epsilon")
        == expected_epsilon_result
    )


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


def test_calculate_rates():
    test_file = "testinput.txt"

    input_list = solution.read_input_file(test_file)

    bit_columns = solution.create_bit_columns(input_list)

    assert solution.calculate_rate(bit_columns, "gamma") == 46
    assert solution.calculate_rate(bit_columns, "epsilon") == 17


def test_calculate_power_consumption():
    test_file = "testinput.txt"

    assert solution.calculate_power_consumption(test_file) == 782
