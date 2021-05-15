import pytest
import requests


def pytest_addoption(parser):
    parser.addoption(
        "--url",
        default="https://ya.ru",
        help="This is default url"
    )
    parser.addoption(
        "--status_codes",
        default=[200, 300, 400, 404, 500, 502],
        help="This is the answer"
    )


@pytest.fixture
def base_url(request):
    return request.config.getoption("--url")


@pytest.fixture
def status_codes(request):
    return getattr(requests, request.config.getoption("--status_codes"))


def test_url_status(base_url, status_codes):
    r = requests.get(base_url)
    r.status_code == status_codes
