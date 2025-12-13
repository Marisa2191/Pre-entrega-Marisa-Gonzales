import requests

BASE_URL = "https://jsonplaceholder.typicode.com"

def test_get_posts_ok():
    response = requests.get(f"{BASE_URL}/posts")

    # 1) Status
    assert response.status_code == 200

    # 2) Estructura
    data = response.json()
    assert isinstance(data, list)
    assert len(data) == 100  # JSONPlaceholder devuelve 100 posts

    # 3) Contenido (chequeo de un item)
    first = data[0]
    assert isinstance(first, dict)

    required_keys = {"userId", "id", "title", "body"}
    assert required_keys.issubset(first.keys())

    assert isinstance(first["userId"], int)
    assert isinstance(first["id"], int)
    assert isinstance(first["title"], str)
    assert isinstance(first["body"], str)
    assert first["title"].strip() != ""

def test_get_post_not_found():
    response = requests.get(f"{BASE_URL}/posts/999999")

    # En JSONPlaceholder, un id inexistente devuelve 404
    assert response.status_code == 404
