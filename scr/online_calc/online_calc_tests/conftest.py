import pytest
from online_calc.online_calc_tools.online_calculator import OnlineCalc
import logging


@pytest.fixture(scope="module")
def Online_Calc_Generic(request):
    Online_Calc_Generic = OnlineCalc()
    Online_Calc_Generic.open_page()

    def fin():
        logging.info("Teardown browser...")
        Online_Calc_Generic.close_browser()
    request.addfinalizer(fin)
    return Online_Calc_Generic
