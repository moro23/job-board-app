import json


def test_create_user(client):
    data = {"username":"testuser","email":"testuser@nofoobar.com","password":"testing"}
    response = client.post("/users/",
    headers={"X-Token": "coneofsilence"},
    json=data
    
    )
    assert response.status_code == 200 
    assert response.json()["email"] == "testuser@nofoobar.com"
    assert response.json()["is_active"] == True

# def test_read_user(client):
#     data = {"username":"testuser",
#     "email":"testuser@nofoobar.com",
#     "password":"testing"}
#     response = client.post("/users/",
#     headers={"X-Token": "coneofsilence"},
#     json=data
    
#     )

#     response = client.get("/users/get/1/")
#     assert response.status_code == 200 
#     assert response.json()['email'] == "testuser@nofoobar.com"