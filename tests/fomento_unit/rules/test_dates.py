from datetime import date
from unittest import mock

import pytest

from src.fomento_unit.rules.dates import get_date_or_default


@pytest.mark.parametrize("val", ["05-6-2022", "5-06-2022", "05-06-2022"])
def test_parse_a_valid_date(val):
    result = get_date_or_default(val)

    assert isinstance(result, date)
    assert result.day == 5
    assert result.month == 6
    assert result.year == 2022


def test_return_today_if_parameter_is_none():
    with mock.patch("src.fomento_unit.rules.dates.get_today_date", return_value=date(2023, 5, 9)) as today:
        result = get_date_or_default(None)

        assert isinstance(result, date)
        assert result.year == 2023
        assert result.month == 5
        assert result.day == 9


@pytest.mark.parametrize("val", ["is-not-date", "31-02-2021", "02/02/2022", "01-01-22"])
def test_return_none_on_invalid_date(val):
    result = get_date_or_default(val)

    assert result is None


def test_date_should_be_gt_01_01_2013():
    lt = get_date_or_default("31-12-2012")

    assert lt is None

    gt = get_date_or_default("01-01-2013")

    assert isinstance(gt, date)
    assert gt.year == 2013
    assert gt.month == 1
    assert gt.day == 1


def test_future_date_is_invalid():
    with mock.patch("src.fomento_unit.rules.dates.get_today_date", return_value=date(2023, 5, 9)):
        result = get_date_or_default("10-08-2023")

        assert result is None
