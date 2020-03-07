
import os
import pytest
import json
from print_n_days_lyrics import generate_lyrics


def test_one_day():
    actual, expected = compare_expected_versus_actual("one_day_expected_output.txt", "one_day.json")
    assert actual == expected


def test_two_days():
    actual, expected = compare_expected_versus_actual("two_days_expected_output.txt", "two_days.json")
    assert actual == expected


def test_twelve_days():
    actual, expected = compare_expected_versus_actual("twelve_days_expected_output.txt", "twelve_days.json")
    assert actual == expected


def compare_expected_versus_actual(expected_output_file, input_json_file):

    if not os.path.exists(expected_output_file) or not os.path.exists(input_json_file):
        pytest.fail("Input files could not be accessed!")

    with open(expected_output_file, "r") as expected, open(input_json_file, "r") as input_file:
        expected_result = expected.read().strip()
        input_json = json.load(input_file)
        actual_result = generate_lyrics(input_json).strip()
        return actual_result, expected_result
