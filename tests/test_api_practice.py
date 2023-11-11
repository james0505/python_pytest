import pytest, warnings
import src.API_practices
from src.API_practices import api_get

def test_request_status():
    assert api_get()["status"] == 200

def test_request_content():
    assert "'completed': False" in api_get()["content"]

def test_api_get_mock_json(mocker):
    # Mock the requests.get function
    mocker_get = mocker.patch("requests.get")
    mocker_get.return_value.status_code = 200
    mocker_get.return_value.json.return_value = {'userId': 1, 'id': 2, 'title': 'quis ut nam facilis et officia qui', 'completed': False}
    assert api_get()["status"] == 200
    assert "'completed': False" in api_get()["content"]

def test_api_get_mock_url(requests_mock, capsys):
    requests_mock.get("https://jsonplaceholder.typicode.com/todos/2", status_code=200, \
        json={'userId': 2, 'id': 2, 'title': 'quis ut nam facilis et officia qui', 'completed': False})
    assert 200 == api_get()["status"]
    assert "'completed': False" in api_get()["content"]
    warnings.warn(str(api_get())) # print warnings in test results
    with capsys.disabled(): #print info in test results using print command
        print(f"api_get returns: {api_get()}")
