import pytest


@pytest.mark.parametrize('src_list,expected_result', [
    (['mango', 'banana', 'melon'], ['melon', 'banana', 'mango']),
    (['a', 'b', 'c'], ['c', 'b', 'a']),
    (['null'], ['null'])
])
def test_reverse(src_list, expected_result):
    src_list.reverse()
    assert src_list == expected_result


def test_append():
    fruits = ['apple', 'banana', 'cherry']
    fruits.append('orange')
    assert fruits == ['apple', 'banana', 'cherry', 'orange']


def test_pop():
    fruits = ['mango', 'banana', 'melon']
    banana = fruits.pop(1)
    assert fruits == ['mango', 'melon']
    assert banana == 'banana'


def test_insert():
    fruits = ['apple', 'banana', 'cherry']
    fruits.insert(1, 'orange')
    assert fruits == ['apple', 'orange', 'banana', 'cherry']


def test_clear():
    berries = ['strawberry', 'raspberry', 'juniper']
    berries.clear()
    assert berries == []
