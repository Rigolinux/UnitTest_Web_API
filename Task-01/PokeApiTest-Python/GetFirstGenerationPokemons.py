import os
import requests
from dotenv import load_dotenv


load_dotenv()


BASE_URL = os.getenv('POKEAPI_BASE_URL')
POKEMON_LIST_URL = f"{BASE_URL}/pokemon?limit=151&offset=0"


def test_status_code_is_200():
    response = requests.get(POKEMON_LIST_URL)
    assert response.status_code == 200, "Expected status code to be 200"


def test_response_is_json_object():
    response = requests.get(POKEMON_LIST_URL)
    try:
        data = response.json()
        assert isinstance(data, dict), "Expected response to be a JSON object"
    except ValueError:
        assert False, "Response is not a valid JSON"


def test_contains_151_pokemon():
    response = requests.get(POKEMON_LIST_URL)
    data = response.json()
    assert len(data['results']) == 151, "Expected response to contain 151 Pokémon"


def test_first_pokemon_is_bulbasaur():
    response = requests.get(POKEMON_LIST_URL)
    data = response.json()
    assert data['results'][0]['name'] == 'bulbasaur', "Expected first Pokémon to be Bulbasaur"


def test_all_pokemon_have_name_and_url():
    response = requests.get(POKEMON_LIST_URL)
    data = response.json()
    for pokemon in data['results']:
        assert 'name' in pokemon, "Expected Pokémon to have a 'name' property"
        assert 'url' in pokemon, "Expected Pokémon to have a 'url' property"


if __name__ == "__main__":
    import pytest
    pytest.main([__file__])

