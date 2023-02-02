import pytest

import library


def test_get_ukrainian_coins():
    assert type(library.get_ukrainian_coins(5)) == str


check_list = [
    (5, 'копійок'),
    (0, 'копійок'),
    (2, 'копійки'),
    (99, 'копійок'),
    (-99, 'копійок'),
]


@pytest.mark.parametrize('test_input, expected', check_list)
def test_get_ukrainian_coins(test_input, expected):
    assert library.get_ukrainian_coins(test_input) == expected


def test_get_ukrainian_hryvnas():
    assert type(library.get_ukrainian_hryvnas(6)) == str


check_list = [
    (6, 'гривень'),
    (22, 'гривні'),
    (32, 'гривні'),
    (199, 'гривень'),
    (-10, 'гривень'),
]


@pytest.mark.parametrize('test_input, expected', check_list)
def test_get_ukrainian_hryvnas(test_input, expected):
    assert library.get_ukrainian_hryvnas(test_input) == expected


def test_get_money():
    assert type(library.get_money(4.01)) == str


check_list = [
    (4.7501, '4 гривні, 75 копійок'),
    (4.3, '4 гривні, 30 копійок'),
    (3.08, '3 гривні, 8 копійок'),
    (4.34, '4 гривні, 34 копійки'),
    (2.0389, '2 гривні, 3 копійки'),
]


@pytest.mark.parametrize('test_input, expected', check_list)
def test_get_money(test_input, expected):
    assert library.get_money(test_input) == expected


def test_is_hot_today():
    assert type(library.is_hot_today(6)) == str


check_list = [
    (10, 'Not hot'),
    (25, 'Not hot'),
    (30, 'Hot'),

]


@pytest.mark.parametrize('test_input, expected', check_list)
def test_is_hot_today(test_input, expected):
    assert library.is_hot_today(test_input) == expected



