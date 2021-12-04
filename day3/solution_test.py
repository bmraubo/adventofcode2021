import pytest
import solution


def test_read_input_file():
    test_file = "testinput.txt"

    expected_result = ["123", "456", "789"]

    assert solution.read_input_file(test_file) == expected_result


def test_create_bit_list():
    test_file = "testinput.txt"

    input_list = solution.read_input_file(test_file)

    expected_result = {0: ["1", "4", "7"], 1: ["2", "5", "8"], 2: ["3", "6", "9"]}

    assert solution.create_bit_columns(input_list) == expected_result
