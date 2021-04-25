import pytest


@pytest.mark.parametrize('src_dict, key, value, expected_result', [
    (
        {'brand': 'Ford', 'model': 'Mustang', 'year': 1964},
        'color',
        'white',
        {'brand': 'Ford', 'model': 'Mustang', 'year': 1964, 'color': 'white'}
    ),
    (
        {'brand': 'Givenchy', 'fragrance': 'Irresistible', 'year': 2020},
        'capacity',
        '50 ml',
        {'brand': 'Givenchy', 'fragrance': 'Irresistible',
            'year': 2020, 'capacity': '50 ml'}
    ),
    (
        {'title': 'Martin Eden', 'author': 'Jack London', 'year': 1909},
        'genre',
        'novel',
        {'title': 'Martin Eden', 'author': 'Jack London',
            'year': 1909, 'genre': 'novel'}
    )
])
def test_update(src_dict, key, value, expected_result):
    src_dict.update({key: value})
    assert src_dict == expected_result


def test_setdefault():
    car = {
        'brand': 'Ford',
        'model': 'Mustang',
        'year': 1964
    }
    car.setdefault('color', 'white')
    assert car['color'] == 'white'
    assert car == {
        'brand': 'Ford',
        'model': 'Mustang',
        'year': 1964,
        'color': 'white'
    }


def test_clear():
    car = {
        'brand': 'Ford',
        'model': 'Mustang',
        'year': 1964
    }
    car.clear()
    assert car == {}


def test_fromkeys():
    keys = ('a', 'b', 'c')
    value = 'letter'
    dictionary = dict.fromkeys(keys, value)
    assert dictionary == {
        'a': 'letter',
        'b': 'letter',
        'c': 'letter'
    }


def test_popitem():
    car = {
        'brand': 'Ford',
        'model': 'Mustang',
        'year': 1964
    }
    item = car.popitem()
    assert car == {
        'brand': 'Ford',
        'model': 'Mustang'
    }
    assert item == ('year', 1964)
