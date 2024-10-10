import pytest
import allure
@allure.title("TC#1 - verify that 2-2 is equal to o")
@allure.description("This is a smoke Testcase which check -verify the assertion")
@pytest.mark.smoke
def test_sub0():
    assert 2-2 ==0