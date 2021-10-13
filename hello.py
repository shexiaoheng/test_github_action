import pytest


def test_one():
    assert 1 == 1


def test_two():
    assert 2 == 2


@pytest.mark.skip
def test_three():
    print('hi')
