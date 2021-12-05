import pytest
from gendiff import generate_diff


@pytest.fixture(name="correct")
def get_correct():
    with open("tests/fixtures/diff.txt") as file:
        correct = file.read()
    return correct


def test_gendiff_plane_json(correct):
    assert generate_diff("tests/fixtures/test1.json", "tests/fixtures/test2.json") == correct


def test_gendiff_plane_yaml(correct):
    assert generate_diff("tests/fixtures/test1.yaml", "tests/fixtures/test2.yaml") == correct
