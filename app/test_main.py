import datetime

import pytest

from app.main import outdated_products


@pytest.fixture
def data_groceries() -> list:
    return [
        {
            "name": "salmon",
            "expiration_date": datetime.date(2022, 2, 10),
            "price": 600
        },
        {
            "name": "chicken",
            "expiration_date": datetime.date(2022, 2, 5),
            "price": 120
        },
        {
            "name": "duck",
            "expiration_date": datetime.date(2022, 2, 1),
            "price": 160
        }
    ]


def test_check_first_outdated_product(data_groceries):
    result = outdated_products(data_groceries)
    assert result == ["salmon", "chicken", "duck"]


def test_check_empty_groceries():
    result = outdated_products([])
    assert result == []


def test_check_valid_groceries(data_groceries):
    data_groceries[0]["expiration_date"] = datetime.date(2025, 2, 3)
    data_groceries[1]["expiration_date"] = datetime.date(2027, 2, 3)
    data_groceries[2]["expiration_date"] = datetime.date(2026, 2, 3)
    result = outdated_products(data_groceries)
    assert result == []


def test_check_invalid_expiration_date(data_groceries):
    data_groceries[0]["expiration_date"] = datetime.date.today()
    data_groceries[1]["expiration_date"] = datetime.date.today()
    data_groceries[2]["expiration_date"] = datetime.date.today()
    result = outdated_products(data_groceries)
    assert result == []


def test_check_expiration_date_equals_yesterday(data_groceries):
    today = datetime.date.today()
    yesterday = today - datetime.timedelta(days=1)
    data_groceries[0]["expiration_date"] = yesterday
    data_groceries[1]["expiration_date"] = yesterday
    data_groceries[2]["expiration_date"] = yesterday
    result = outdated_products(data_groceries)
    assert result == ["salmon", "chicken", "duck"]