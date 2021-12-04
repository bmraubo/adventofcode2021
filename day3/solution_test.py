import pytest
import solution


def test_read_input_file():
    test_file = "testinput.txt"

    expected_result = ["1011", "0101", "1010"]

    assert solution.read_input_file(test_file) == expected_result


def test_create_bit_list():
    test_file = "testinput.txt"

    input_list = solution.read_input_file(test_file)

    expected_result = {
        0: ["1", "0", "1"],
        1: ["0", "1", "0"],
        2: ["1", "0", "1"],
        3: ["1", "1", "0"],
    }

    assert solution.create_bit_columns(input_list) == expected_result
