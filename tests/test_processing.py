import pytest
from src.processing import filter_by_state, sort_by_date


def test_filter_by_state():
    assert filter_by_state([
            {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
            {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
            {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        ],
        "EXECUTED") == [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
                        {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]


@pytest.fixture()
def dict_invalid():
    return [{"id": 594226727, "stat": "EXECUTED", "date": "2018-09-12T21:27:25.241689"},
            {"id": 594226727, "state": "EXECUTE", "date": "2018-09-12T21:27:25.241689"},
            {"id": 594226727, "": "EXECUTED", "date": "2018-09-12T21:27:25.241689"},
            {"id": 594226727, "state": "", "date": "2018-09-12T21:27:25.241689"},
            {"id": 594226727, "date": "2018-09-12T21:27:25.241689"},
            {}]
def test_filter_by_state_invalid(dict_invalid):
    assert filter_by_state(dict_invalid, "EXECUTED") == []


@pytest.mark.parametrize('list_dict, value, expected', [([{"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                                                         {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"}], 'EXECUTED',
                                                        [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}]),
                                                        ([{"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                                                          {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"}], 'CANCELED',
                                                         [{"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"}])])
def test_filter_by_state_invalid_different(list_dict, value, expected):
    assert filter_by_state(list_dict, value) == expected


def test_sort_by_date_true():
    assert sort_by_date([
            {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
            {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
            {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        ],
        True) == [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
                  {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
                  {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
                  {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]


def test_sort_by_date_false():
    assert sort_by_date([
            {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
            {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
            {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        ],
        False) == [{"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                   {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                  {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
                  {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"}]


def test_sort_by_date_true_same_dates():
    assert (sort_by_date([
            {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
            {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
            {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},]) ==
            [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
            {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
            {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
            {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}])


@pytest.mark.parametrize('list_dict, parameter, expected', [([{"id": 41428829, "state": "EXECUTED" , '' : "2019-07-03T18:35:29.512364"},
                                                              {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                                                              {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"}], True,
                                                             [{"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                                                              {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                                                              {"id": 41428829, "state": "EXECUTED" , '' : "2019-07-03T18:35:29.512364"}]),
                                                            ([{"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                                                             {"id": 594226727, "state": "CANCELED"},
                                                             {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"}], True,
                                                            [{"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
                                                            {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                                                             {"id": 594226727, "state": "CANCELED"}]),
                                                            ([{"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                                                             {"id": 594226727, "state": "CANCELED", "date": ""},
                                                             {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"}], True,
                                                            [{"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
                                                            {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                                                             {"id": 594226727, "state": "CANCELED", "date": ""}])])
def test_sort_by_date_invalid_date(list_dict, parameter, expected):
    assert sort_by_date(list_dict, parameter) == expected
