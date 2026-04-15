from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_get_items_returns_200():
    response = client.get("/api/v1/items/")
    assert response.status_code == 200


def test_create_item_returns_201():
    payload = {"name": "Pytest Item", "description": "Created by pytest"}

    response = client.post("/api/v1/items/", json=payload)

    assert response.status_code == 201

    data = response.json()
    assert data["name"] == "Pytest Item"
    assert data["description"] == "Created by pytest"
    assert "id" in data


def test_get_item_by_id_returns_200():
    create_payload = {"name": "Fetch Me", "description": "Item to fetch by id"}

    create_response = client.post("/api/v1/items/", json=create_payload)
    created_item = create_response.json()

    item_id = created_item["id"]

    response = client.get(f"/api/v1/items/{item_id}")
    assert response.status_code == 200

    data = response.json()
    assert data["id"] == item_id
    assert data["name"] == "Fetch Me"


def test_update_item_returns_200():
    create_payload = {"name": "Old Name", "description": "Before update"}

    create_response = client.post("/api/v1/items/", json=create_payload)
    created_item = create_response.json()

    item_id = created_item["id"]

    update_payload = {"name": "Updated Name", "description": "After update"}

    response = client.put(f"/api/v1/items/{item_id}", json=update_payload)
    assert response.status_code == 200

    data = response.json()
    assert data["id"] == item_id
    assert data["name"] == "Updated Name"
    assert data["description"] == "After update"


def test_delete_item_returns_204():
    create_payload = {"name": "Delete Me", "description": "Item to delete"}

    create_response = client.post("/api/v1/items/", json=create_payload)
    created_item = create_response.json()

    item_id = created_item["id"]

    delete_response = client.delete(f"/api/v1/items/{item_id}")
    assert delete_response.status_code == 204

    get_response = client.get(f"/api/v1/items/{item_id}")
    assert get_response.status_code == 404


def test_get_item_by_id_returns_404_when_not_found():
    response = client.get("/api/v1/items/999999")
    assert response.status_code == 404
    assert response.json()["detail"] == "Item not found"


def test_update_item_returns_404_when_not_found():
    payload = {"name": "Does Not Exist", "description": "No item here"}

    response = client.put("/api/v1/items/999999", json=payload)
    assert response.status_code == 404
    assert response.json()["detail"] == "Item not found"


def test_delete_item_returns_404_when_not_found():
    response = client.delete("/api/v1/items/999999")
    assert response.status_code == 404
    assert response.json()["detail"] == "Item not found"
