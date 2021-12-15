import pytest

from gendiff import generate_diff


@pytest.fixture(name="correct_plane")
def get_correct_plain():
    with open("tests/fixtures/diff_plane.txt") as file:
        correct_plane = file.read()
    return correct_plane


@pytest.fixture(name="correct_recursive")
def get_correct_recursive():
    with open("tests/fixtures/diff_plane.txt") as file:
        correct_recursive = file.read()
    return correct_recursive


def test_gendiff_plane_json(correct_plane):
    assert generate_diff("tests/fixtures/test_plane1.json", "tests/fixtures/test_plane2.json") == correct_plane


def test_gendiff_plane_yaml(correct_plane):
    assert generate_diff("tests/fixtures/test_plane1.yaml", "tests/fixtures/test_plane2.yaml") == correct_plane


def test_gendiff_recursive_yaml(correct_recursive):
    assert generate_diff("tests/fixtures/test_recursive1.yaml",
                         "tests/fixtures/test_recursive2.yaml") == correct_recursive


def test_gendiff_recursive_json(correct_recursive):
    assert generate_diff("tests/fixtures/test_recursive1.json",
                         "tests/fixtures/test_recursive2.json") == correct_recursive
