import pytest

@pytest.mark.parametrize("str,expected_result", [
    ('abc', 'Abc'),
    ('xyz', 'Xyz'),
    ('qwerty', 'Qwerty')
])
def test_capitalize(str, expected_result):
    capitalized = str.capitalize()
    assert capitalized == expected_result

def test_find():
    str = 'London is the capital of Great Britain'
    found_index = str.find('of')
    assert found_index == 22

def test_replace():
    str = 'London is the capital of the United Kingdom'
    replaced = str.replace('the United Kingdom', 'Great Britain')
    assert replaced == 'London is the capital of Great Britain'

def test_split():
    str = 'London is the capital of the United Kingdom'
    split_result = str.split()
    assert split_result == ['London', 'is', 'the', 'capital', 'of', 'the', 'United', 'Kingdom']

def test_count():
    str = 'Berlin is the capital of Germany'
    count_of_e = str.count('e')
    assert count_of_e == 3