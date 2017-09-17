import pytest
import logging

# Global variables
PAGE_TITLE = r"Web 2.0 scientific calculator"


def test_page_title(Online_Calc_Generic, title=PAGE_TITLE):
    """
    This test checks opened page title.
    :param Online_Calc_Generic: Online calc fixture from conftest.py
    :param title: expected page title
    """
    assert title in Online_Calc_Generic.driver.title, logging.error("Page title was incorrect")


@pytest.mark.parametrize("x", [0, 1])
@pytest.mark.parametrize("y", [2, 3])
def test_addition(Online_Calc_Generic, x, y):
    """
    This tests checks if addition feature of Online_Calc works correctly.
    :param Online_Calc_Generic: Online calc fixture from conftest.py
    :param x: first operation variable
    :param y: second operation variable
    """
    result = Online_Calc_Generic.addition(x, y)
    assert result == x+y, logging.error("Addition result was incorrect")


@pytest.mark.parametrize("x", [5, 3])
@pytest.mark.parametrize("y", [9, 4])
def test_substraction(Online_Calc_Generic, x, y):
    """
    This tests checks if substraction feature of Online_Calc works correctly.
    :param Online_Calc_Generic: Online calc fixture from conftest.py
    :param x: first operation variable
    :param y: second operation variable
    """
    result = Online_Calc_Generic.substraction(x, y)
    assert result == x-y, logging.error("Substraction result was incorrect")


@pytest.mark.parametrize("x", [4, 8])
@pytest.mark.parametrize("y", [2, 6])
def test_division(Online_Calc_Generic, x, y):
    """
    This tests checks if division feature of Online_Calc works correctly.
    :param Online_Calc_Generic: Online calc fixture from conftest.py
    :param x: first operation variable
    :param y: second operation variable
    """
    result = Online_Calc_Generic.division(x, y)
    assert result == round(x/y,2), logging.error("Division result was incorrect")


@pytest.mark.parametrize("x", [0, 1])
@pytest.mark.parametrize("y", [3, 2])
def test_multiplication(Online_Calc_Generic, x, y):
    """
    This tests checks if multiplication feature of Online_Calc works correctly.
    :param Online_Calc_Generic: Online calc fixture from conftest.py
    :param x: first operation variable
    :param y: second operation variable
    """
    result = Online_Calc_Generic.multiplication(x, y)
    assert result == x*y, logging.error("Multiplication result was incorrect")

if __name__ == "__main__":
    pytest.main()