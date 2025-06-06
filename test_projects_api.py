import requests
import pytest

BASE_URL = "https://yougile.com/api-v2/projects"
HEADERS = {
    "Content-Type": "application/json",
    "Accept": "application/json",
    "Authorization": "Bearer 6tus3axdAtUjfUCrYb8MxxRjkVpnawspCLJ+zJEi4HzZolJBPEWUACg3ePqAhsNo"
}

@pytest.fixture
def new_project():
    payload = {"title": "Autotest Project"}
    response = requests.post(BASE_URL, json=payload, headers=HEADERS, verify=False)
    response.raise_for_status()
    return response.json()

def test_create_project_positive():
    payload = {"title": "Первый проект"}
    response = requests.post(BASE_URL, json=payload, headers=HEADERS, verify=False)
    assert response.status_code == 201

def test_create_project_negative():
    payload = {}
    response = requests.post(BASE_URL, json=payload, headers=HEADERS, verify=False)
    assert response.status_code == 400 or response.status_code == 422

def test_update_project_positive(new_project):
    project_id = new_project["id"]
    payload = {"title": "Updated Name"}
    response = requests.put(f"{BASE_URL}/{project_id}", json=payload, headers=HEADERS, verify=False)
    assert response.status_code == 200

def test_update_project_invalid_id():
    response = requests.put(f"{BASE_URL}/invalid_id", json={"name": "Name"}, headers=HEADERS, verify=False)
    assert response.status_code in (400, 404)

def test_get_project_positive(new_project):
    project_id = new_project["id"]
    response = requests.get(f"{BASE_URL}/{project_id}", headers=HEADERS, verify=False)
    assert response.status_code == 200

def test_get_project_invalid_id():
    response = requests.get(f"{BASE_URL}/invalid_id", headers=HEADERS, verify=False)
    assert response.status_code in (400, 404)
