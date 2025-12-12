import pytest

@pytest.mark.sanitypyets
def test_login_with_email():
    print("test_login_with_email")

@pytest.mark.order(1)
def test_login_with_phone():
    print("test_login_with_phone")

@pytest.mark.regression
def test_login_with_facebook():
    print("test_login_with_facebook")

