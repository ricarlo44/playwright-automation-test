import pytest
from playwright.sync_api import *

@pytest.fixture
def api_context(playwright: Playwright): 
    api_context = playwright.request.new_context(base_url="https://dummyjson.com",
                                                 extra_http_headers={'Content-Type':'application/json'})
    yield api_context
    api_context.dispose()

def test_create_user(api_context: APIRequestContext):
    response = api_context.post("users/add",
                     data={"firstName": "Damien","lastName": "Smith", "age": 27})
    #response = api_context.post(f"users/search?q={query}")
    #response = api_context.post("users/add")
    
    users_data = response.json()

    #for user in users_data["users"]:
    print(f"\n {users_data}")
    #    #print("Checking user:", user["firstName"])
    assert users_data["id"] == 209
    assert users_data["firstName"] == "Damien"

def test_update_user(api_context: APIRequestContext):

    print(api_context.get("user/1").json()["lastName"]) 
    
    response = api_context.put("users/1", data={"lastName": "Smith", "age": 20})
    user_data = response.json()

    print(user_data)

    assert user_data["lastName"] == "Smith"
    assert user_data["age"] == 20

