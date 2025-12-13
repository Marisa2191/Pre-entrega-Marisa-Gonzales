import requests

BASE_URL = "https://jsonplaceholder.typicode.com"

def test_delete_post():
    post_id = 1

    response = requests.delete(f"{BASE_URL}/posts/{post_id}")

    # JSONPlaceholder responde 200 (a veces 204 en otras APIs, pero acá suele ser 200)
    assert response.status_code in (200, 204)

    # Muchas APIs devuelven body vacío en DELETE.
    # En JSONPlaceholder normalmente devuelve {}.
    if response.text.strip():
        data = response.json()
        assert isinstance(data, dict)
