import random

import pytest
import requests


def test_get_resource():
    r = requests.get('https://jsonplaceholder.typicode.com/posts/1')
    assert r.status_code == requests.codes.ok


@pytest.mark.parametrize('baseUrl', ['https://jsonplaceholder.typicode.com/posts'])
def test_all_resource(baseUrl):
    r = requests.get(baseUrl)
    assert r.status_code == requests.codes.ok


@pytest.mark.parametrize('baseUrl', 'idN', ['https://jsonplaceholder.typicode.com/posts/'], ['1', '2', '3'])
def test_all_resource(baseUrl, idN):
    r = requests.get(baseUrl + idN)
    assert r.status_code == requests.codes.ok


@pytest.mark.parametrize('input_id, output_id',
                         [(10000, '10000'),
                          (-1, '-1'),
                          (0, '0')])
@pytest.mark.parametrize('input_title, output_title',
                         [('title', 'title'),
                          ('', ''),
                          (100, '100'),
                          ('&', '&')])
def test_create_resource(input_id, output_id, input_title, output_title):
    r = requests.post('https://jsonplaceholder.typicode.com/posts',
                      data={'title': input_title, 'body': 'bar', 'userId': input_id})
    res_json = res.json()
    assert res_json['title'] == output_title
    assert res_json['body'] == 'bar'
    assert res_json['userId'] == output_id


@pytest.mark.parametrize('baseUrl', ['https://jsonplaceholder.typicode.com/posts/'])
@pytest.mark.parametrize('userId, userId_in_response', [(1, 1), (2, 2), (10, 10)])
def test_api_filtering(baseUrl, userId, userId_in_response):
    response = requests.get(
        baseUrl + "/posts",
        params={'userId': userId}
    ).json()
    random_post_number = random.randint(1, 9)
    assert len(response) > 0
    assert response[random_post_number]['userId'] == userId_in_response
