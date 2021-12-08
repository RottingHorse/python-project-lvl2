import pytest
from gendiff import generate_diff


@pytest.fixture(name="correct_plain")
def get_correct_plain():
    with open("tests/fixtures/diff_plain.txt") as file:
        correct_plain = file.read()
    return correct_plain


@pytest.fixture(name="correct_recursive")
def get_correct_recursive():
    with open("tests/fixtures/diff_plain.txt") as file:
        correct_recursive = file.read()
    return correct_recursive


def test_gendiff_plane_json(correct_plain):
    assert generate_diff("tests/fixtures/test_plain1.json", "tests/fixtures/test_plain2.json") == correct_plain


def test_gendiff_plane_yaml(correct_plain):
    assert generate_diff("tests/fixtures/test_plain1.yaml", "tests/fixtures/test_plain2.yaml") == correct_plain


def test_gendiff_recursive_yaml(correct_recursive):
    assert generate_diff("tests/fixtures/test_recursive1.yaml",
                         "tests/fixtures/test_recursive2.yaml") == correct_recursive


def test_gendiff_recursive_json(correct_recursive):
    assert generate_diff("tests/fixtures/test_recursive1.json",
                         "tests/fixtures/test_recursive2.json") == correct_recursive
