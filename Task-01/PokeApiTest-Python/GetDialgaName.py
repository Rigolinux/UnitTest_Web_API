import os
import requests
from dotenv import load_dotenv


load_dotenv()


BASE_URL = os.getenv('POKEAPI_BASE_URL')
POKEMON_DIALGA_URL = f"{BASE_URL}/pokemon/dialga"


def test_pokemon_id_is_483():
    response = requests.get(POKEMON_DIALGA_URL)
    data = response.json()
    assert data['id'] == 483, "Expected Pokémon ID to be 483"


def test_pokemon_has_steel_type():
    response = requests.get(POKEMON_DIALGA_URL)
    data = response.json()
    has_steel_type = any(type_info['type']['name'] == 'steel' for type_info in data['types'])
    assert has_steel_type, "Expected Pokémon to have 'steel' type"


def test_response_size_below_200kb():
    response = requests.get(POKEMON_DIALGA_URL)
    response_size_kb = len(response.content) / 1024  # Convertir a KB
    assert response_size_kb < 200, f"Expected response size to be below 200KB, but got {response_size_kb}KB"


def test_response_time_below_200ms():
    response = requests.get(POKEMON_DIALGA_URL)
    response_time_ms = response.elapsed.total_seconds() * 1000  # Convertir a milisegundos
    assert response_time_ms < 200, f"Expected response time to be below 200ms, but got {response_time_ms}ms"


def test_response_body_not_empty():
    response = requests.get(POKEMON_DIALGA_URL)
    assert response.text, "Expected response body to not be empty"


if __name__ == "__main__":
    import pytest
    pytest.main([__file__])

