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


def test_find_most_common():
    test_file = "testinput.txt"

    input_list = solution.read_input_file(test_file)

    bit_columns = solution.create_bit_columns(input_list)

    expected_result = ["1", "0", "1", "1", "1", "0"]

    assert solution.find_most_common(bit_columns) == expected_result


def test_convert_list_to_string():
    test_input = ["1", "0", "1", "1", "1", "0"]

    assert solution.convert_list_to_string(test_input) == "101110"
