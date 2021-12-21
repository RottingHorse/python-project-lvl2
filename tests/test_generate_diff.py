import pytest
import json

from gendiff import generate_diff


def get_correct(correct_file):
    with open(correct_file) as file:
        return file.read()


def get_correct_json(correct_file):
    with open(correct_file) as file:
        return json.loads(file.read())


testdata = [
    ("tests/fixtures/test_plane1.json", "tests/fixtures/test_plane2.json",
     "stylish",
     "tests/fixtures/diff_plane.txt"),
    ("tests/fixtures/test_plane1.yaml", "tests/fixtures/test_plane2.yaml",
     "stylish",
     "tests/fixtures/diff_plane.txt"),
    ("tests/fixtures/test_recursive1.json",
     "tests/fixtures/test_recursive2.json", "stylish",
     "tests/fixtures/diff_recursive.txt"),
    ("tests/fixtures/test_recursive1.yaml",
     "tests/fixtures/test_recursive2.yaml", "stylish",
     "tests/fixtures/diff_recursive.txt"),
    ("tests/fixtures/test_recursive1.json",
     "tests/fixtures/test_recursive2.json", "plain",
     "tests/fixtures/diff_nested_plain.txt"),
    ("tests/fixtures/test_recursive1.yaml",
     "tests/fixtures/test_recursive2.yaml", "plain",
     "tests/fixtures/diff_nested_plain.txt")
]

testdata_json = [("tests/fixtures/test_recursive1.json",
                  "tests/fixtures/test_recursive2.json", "json",
                  "tests/fixtures/diff_nested_json.txt"),
                 ("tests/fixtures/test_recursive1.yaml",
                  "tests/fixtures/test_recursive2.yaml", "json",
                  "tests/fixtures/diff_nested_json.txt")]


@pytest.mark.parametrize("file1, file2, fmt, correct_file", testdata)
def test_gendiff_string_formatters(file1, file2, fmt, correct_file):
    correct = get_correct(correct_file)
    assert generate_diff(file1, file2, fmt) == correct


@pytest.mark.parametrize("file1, file2, fmt, correct_file", testdata_json)
def test_gendiff_json_formatter(file1, file2, fmt, correct_file):
    correct = get_correct_json(correct_file)
    assert json.loads(generate_diff(file1, file2, fmt)) == correct
