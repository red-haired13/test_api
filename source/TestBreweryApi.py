import pytest
import requests
from attr.setters import validate


@pytest.mark.parametrize('baseUrl', 'https://api.openbrewerydb.org/breweries')
def test_brewery_status(baseUrl):
    r = requests.get(baseUrl)
    print(r.status_code == requests.codes.ok)


@pytest.mark.parametrize('bre', ['9094', '11767', '14677'])
def test_one_brewery(bre):
    r = requests.get("https://api.openbrewerydb.org/breweries/" + bre)


@pytest.mark.parametrize(('baseUrl', 'attr'), ('https://api.openbrewerydb.org/breweries/search?query=', 'cat')

                         )
def test_brewery_query(baseUrl, attr):
    r = requests.get(baseUrl + attr)


def test_brewery_auto():
    r = requests.get('https: // api.openbrewerydb.org / breweries / autocomplete?query = dog')

def test_api_brewery_negative():
    r = requests.get('https://api.openbrewerydb.org/breweries/5494')
    schema = {
        "type": "object",
        "properties": {
            "message": {"type": "string"},
        },
        "required": ["message", "status"]
    }
    validate(instance=r.json(), schema=schema)
