import pytest


@pytest.mark.parametrize('src_set, new_member, expected_result', [
    ({1, 2, 3}, 4, {1, 2, 3, 4}),
    ({'a', 'b', 'c'}, 'a', {'a', 'b', 'c'}),
    ({'a', 'b', ('a', 'b')}, 'd', {'a', 'b', ('a', 'b'), 'd'}),
    (set(), 'empty_set', {'empty_set'})
])
def test_add(src_set, new_member, expected_result):
    src_set.add(new_member)
    assert src_set == expected_result


def test_is_member():
    test_set = {1, 2, 3}
    assert 3 in test_set
    assert 5 not in test_set


def test_remove():
    test_set = {1, 2, 3}
    test_set.remove(2)
    assert test_set == {1, 3}


def test_intersection():
    set1 = {1, 2, 3}
    set2 = {1, 'a', 'b', 3}
    result = set1.intersection(set2)
    assert result == {1, 3}


def test_difference():
    set1 = {1, 2, 3}
    set2 = {1, 'a', 'b', 3}
    result = set1.difference(set2)
    assert result == {2}
