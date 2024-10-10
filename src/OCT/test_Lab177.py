import pytest
import allure
import requests

@allure.title("Test GET Request -#1")
@allure.description("Positive TC")
@allure.tag("regression","p0","soke")
@allure.label("Owner", "Akshay Kumar")
@allure.testcase("TC#1")
@pytest.mark.smoke
def test_get_single_request_by_id1():
    url ="https://restful-booker.herokuapp.com/booking/1"
    response_Data =requests.get(url)
    print(response_Data)
    print(response_Data.json())
    assert response_Data.status_code == 200
@allure.title("Test GET Request -#2")
@allure.description("Negative TC")
@allure.tag("regression","p0","soke")
@allure.label("Owner", "Akshay Kumar")
@allure.testcase("TC#2")
@pytest.mark.smoke
def test_get_single_request_by_id2():
    url ="https://restful-booker.herokuapp.com/booking/invalid"
    response_Data =requests.get(url)
    print(response_Data)
    assert response_Data.status_code == 404
@allure.title("Test GET Request -#3")
@allure.description("Negative TC")
@allure.tag("regression","p0","soke")
@allure.label("Owner", "Akshay Kumar")
@allure.testcase("TC#3")
@pytest.mark.smoke
def test_get_single_request_by_id3():
    url ="https://restful-booker.herokuapp.com/booking/-1"
    response_Data =requests.get(url)
    print(response_Data)
    assert response_Data.status_code == 404