import requests

BASE_URL = "https://jsonplaceholder.typicode.com"

def test_create_post_ok():
    payload = {
        "userId": 1,
        "title": "Test QA Automation",
        "body": "Creando post desde pytest con requests"
    }

    response = requests.post(f"{BASE_URL}/posts", json=payload)

    # 1) Status (éxito)
    assert response.status_code in (201, 200)

    # 2) Estructura
    data = response.json()
    assert isinstance(data, dict)

    # 3) Contenido
    assert "id" in data
    assert isinstance(data["id"], int)

    # JSONPlaceholder suele “devolver” lo enviado
    assert data.get("title") == payload["title"]
    assert data.get("body") == payload["body"]
    assert data.get("userId") == payload["userId"]
    
def test_create_post_error_endpoint():
    payload = {
        "userId": 1,
        "title": "Post inválido",
        "body": "Probando error"
    }

    response = requests.post(f"{BASE_URL}/posts_invalido", json=payload)

    # Escenario de error
    assert response.status_code == 404
