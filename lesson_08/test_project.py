import requests
import pytest

BASE_URL = "https://ru.yougile.com/api-v2"

LOGIN =
PASSWORD =
COMPANY_ID =


def get_api_token():
    payload = {
        "login": LOGIN,
        "password": PASSWORD,
        "companyId": COMPANY_ID
    }

    response = requests.post(f"{BASE_URL}/auth/keys/get", json=payload)

    assert response.status_code == 200

    keys_list = response.json()

    latest = keys_list[-1]
    token = latest.get("key")

    assert token is not None

    return token


@pytest.fixture(scope="session")
def auth_headers():
    token = get_api_token()
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }
    return headers


def create_project_response(auth_headers, title='Новый проект'):
    return requests.post(f"{BASE_URL}/projects",
                         json={'title': title}, headers=auth_headers)


def create_new_project(auth_headers, title="Новый проект"):
    response = create_project_response(auth_headers, title)
    assert response.status_code == 201, response.text
    return response.json()["id"]


def test_create_project_positive(auth_headers):
    response = create_project_response(auth_headers, title='Test1')
    assert response.status_code == 201, response.text
    body = response.json()
    assert "id" in body
    project_id = body["id"]

    requests.delete(f"{BASE_URL}/projects/{project_id}", headers=auth_headers)


def test_create_project_negative(auth_headers):
    response = create_project_response(auth_headers, title='')
    assert response.status_code == 400, response.text
    body = response.json()
    assert "title should not be empty" in body["message"]


def test_edit_project_positive(auth_headers):
    project_id = create_new_project(auth_headers, title='hot dog')
    print(f"Создан проект с ID:{project_id}")
    body_for_edit = {
        'title': 'cold dog'
    }
    response = requests.put(f"{BASE_URL}/projects/{project_id}",
                            json=body_for_edit, headers=auth_headers)
    assert response.status_code == 200
    assert response.json()["id"] == project_id

    get_response = requests.get(f"{BASE_URL}/projects/{project_id}",
                                headers=auth_headers)
    assert get_response.status_code == 200, get_response.text
    assert get_response.json()['title'] == 'cold dog'


def test_edit_project_negative(auth_headers):
    project_id = create_new_project(auth_headers, title='hottest')
    body_for_edit = {
        'title': ''
    }
    response = requests.put(f"{BASE_URL}/projects/{project_id}",
                            json=body_for_edit, headers=auth_headers)
    assert response.status_code == 400


def test_get_info_project_positive(auth_headers):
    project_id = create_new_project(auth_headers)
    response = requests.get(f"{BASE_URL}/projects/{project_id}",
                            headers=auth_headers)
    assert response.status_code == 200


def test_get_info_project_negative(auth_headers):
    project_id = '4f6f0391-0f94-4d30-9b0e-99430a36d4fb'
    response = requests.get(f"{BASE_URL}/projects/{project_id}",
                            headers=auth_headers)
    assert response.status_code == 404
