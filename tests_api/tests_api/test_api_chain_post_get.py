import requests

BASE_URL = "https://jsonplaceholder.typicode.com"


def test_chain_create_post_then_get():
    # 1) Crear recurso (POST)
    payload = {
        "userId": 1,
        "title": "Chain Test - QA Automation",
        "body": "Creando post y luego intentando obtenerlo (POST -> GET)."
    }

    post_resp = requests.post(f"{BASE_URL}/posts", json=payload)

    # Status POST (éxito)
    assert post_resp.status_code in (201, 200)

    post_data = post_resp.json()
    assert isinstance(post_data, dict)

    # Validar que devuelve un id
    assert "id" in post_data
    assert isinstance(post_data["id"], int)

    created_id = post_data["id"]

    # Validar que devuelve lo enviado (JSONPlaceholder suele devolverlo)
    assert post_data.get("title") == payload["title"]
    assert post_data.get("body") == payload["body"]
    assert post_data.get("userId") == payload["userId"]

    # 2) Intentar obtener el recurso creado (GET)
    get_resp = requests.get(f"{BASE_URL}/posts/{created_id}")

    # En JSONPlaceholder, el POST no persiste: el GET puede devolver 200 o 404.
    assert get_resp.status_code in (200, 404)

    if get_resp.status_code == 200:
        get_data = get_resp.json()
        assert isinstance(get_data, dict)
        assert get_data["id"] == created_id
    else:
        # Si es 404, sigue siendo válido para este TP porque la API no persiste recursos.
        assert get_resp.text is not None
