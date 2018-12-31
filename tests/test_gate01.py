"""
This gate is about receive and handle arguments from URL.
"""
from pytest import mark

import requests

from . import URL


@mark.gate01
@mark.parametrize('expect', ['hello', 'world'])
def test_001_echo(expect):
    """
    This case is about receiving parameters in URLs.

    URL example: http://localhost:8888/echo?msg=hello
    """
    response = requests.get(URL + '/echo', params={'msg': expect})
    response.raise_for_status()
    assert expect == response.content.decode()


@mark.gate01
@mark.parametrize('name , gender', [
    ('Alice', 'Female'),
    ('Bob', 'Male'),
])
def test_002_gender(name, gender):
    """
    You need to treat a part of URL as a parameter in this case.

    URL example: http://localhost:8888/gender/Alice
    """
    response = requests.get('{}/gender/{}'.format(URL, name))
    response.raise_for_status()
    assert gender == response.content.decode()


@mark.gate01
@mark.parametrize(
    'username, password', [
        ('Alice', 'batman'),
        ('Bob', '123456'),
    ]
)
def test_003_form(username, password):
    """
    A form is submitted, and you need to handle it.

    URL example: http://localhost:8888/form
    """
    response = requests.post(
        URL + '/form',
        data={
            'username': username,
            'password': password,
        },
    )
    response.raise_for_status()
    result = response.json()
    assert result['user'] == username
    assert result['pass'] == password
