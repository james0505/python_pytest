#import logging
##logging.basicConfig(filename="./my_logger.log", level=logging.DEBUG)
#logger = logging.getLogger(__name__)
#console_handler =logging.StreamHandler()
#logger.addHandler(console_handler)
import pytest
import src.myfunctions
from src.myfunctions import get_operating_system, double, slow_dataset, sum_two_numbers

# Test cases
@pytest.mark.test_id("T1200")
@pytest.mark.parametrize("_", [0], ids=["10"])
def test_get_operationg_system(_):
    """Function to test get_operating_sytem function without using mock
    :param: None
    :return: None
    """
    # logger.info("testRuslts: \n")
    assert get_operating_system() == "Windows"

@pytest.mark.test_id("T1201")
def test_get_operating_system_mock(mocker):
    """Function to test get_operating_sytem function with mock
    :param: mocker
    :return: None
    """
    mocker.patch('src.myfunctions.is_windows', return_value = True)
    assert get_operating_system() == "Windows"

@pytest.mark.test_id("T1202")
def test_double(mocker):
    """Function to test double
    Args:
        mocker (_type_): mocker object
    """
    # given
    mocker.patch.object(src.myfunctions, 'CONSTANT_A', 5)
    # when
    result = double()
    # then
    assert result == 10

@pytest.mark.test_id("T1203")   
@pytest.mark.regression
def test_slow_dataset(mocker):
    """Function to test slow_dataset function
    Args:
        mocker (_type_): mocker object
    """
    mocker.patch("src.myfunctions.Dataset.load_data", return_value = "slow data")
    assert slow_dataset() == "slow data"

@pytest.mark.test_id("T1204")
@pytest.mark.parametrize("a, b, expected", [(1, 2, 3), (4, 6, 10), (0, 555.6,  555.6)], ids=[11, 12,13])
def test_sum_two_numbers(a, b, expected):
    """test function of sum_two_numbers using parameterize fixture

    Args:
        a (d): the first operand
        b (d): the second operand
        expected (d): sum
    """
    assert sum_two_numbers(a, b) == expected
