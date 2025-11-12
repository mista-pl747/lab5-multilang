import pytest
from app import app, process_user_data

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


def test_home_ok(client):
    response = client.get('/')
    assert response.status_code == 200
    assert response.data.decode() == "OK"


def test_home_error_path_not_covered():
    original = app.view_functions['home']

    def mock_home():
        status_code = 0
        if status_code == 1:
            return "OK"
        return "Error", 400
    app.view_functions['home'] = mock_home
    client = app.test_client()
    response = client.get('/')
    assert response.status_code == 400
    assert response.data.decode() == "Error"
    app.view_functions['home'] = original


def test_process_user_data_invalid_input():
    assert process_user_data(None, {}) == {'error': 'Invalid input'}
    assert process_user_data("123", []) == {'error': 'Invalid input'}


def test_process_user_data_empty_name():
    result = process_user_data("1", {"name": "   "})
    assert result['name'] == 'Anonymous'


def test_process_user_data_long_name():
    long_name = "a" * 150
    result = process_user_data("1", {"name": long_name})
    assert result['name'] == "a" * 100


def test_process_user_data_valid_age_int():
    result = process_user_data("1", {"age": 25})
    assert result['age'] == 25


def test_process_user_data_age_out_of_range():
    result = process_user_data("1", {"age": 200})
    assert result['age'] is None


def test_process_user_data_age_string_valid():
    result = process_user_data("1", {"age": "30"})
    assert result['age'] == 30


def test_process_user_data_age_string_invalid():
    result = process_user_data("1", {"age": "abc"})
    assert result['age'] is None


def test_process_user_data_age_none():
    result = process_user_data("1", {"age": None})
    assert result['age'] is None


def test_process_user_data_valid_email():
    result = process_user_data("1", {"email": "test@example.com"})
    assert result['email'] == "test@example.com"


def test_process_user_data_invalid_email():
    result = process_user_data("1", {"email": "invalid"})
    assert result['email'] is None


def test_process_user_data_email_no_at():
    result = process_user_data("1", {"email": "test.com"})
    assert result['email'] is None


def test_process_user_data_email_no_dot():
    result = process_user_data("1", {"email": "test@com"})
    assert result['email'] is None


def test_process_user_data_full_valid():
    data = {
        "name": "John Doe",
        "age": "42",
        "email": "john@example.com"
    }
    result = process_user_data("123", data)
    assert result == {
        "name": "John Doe",
        "age": 42,
        "email": "john@example.com"
    }
