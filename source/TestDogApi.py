import pytest
import requests
import cerberus
from attr.setters import validate


def test_api_status_code():
    r = requests.get('https://dog.ceo/api/breed/hound/list/all')
    assert r.status_code == requests.codes.ok


def test_api_all_breed(base_url):
    """Проверка ответа на запрос списка всех пород"""
    res = requests.get('https://dog.ceo/api/breed/hound/list/all')

    schema = {
        "message": [
            "afghan",
            "basset",
            "blood",
            "english",
            "ibizan",
            "plott",
            "walker"
        ],
        "status": "success"
    }

    v = cerberus.Validator()
    assert v.validate(res.json(), schema)


def test_api_random_schema():
    r = requests.get('https://dog.ceo/api/breeds/image/random')
    schema = {
        "type": "object",
        "properties": {
            "message": {"type": "string"},
            "status": {"type": "string"}
        },
        "required": ["message", "status"]
    }
    validate(instance=r.json(), schema=schema)
