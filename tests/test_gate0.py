"""
This is just a beginning.
Enjoy the journey O(∩_∩)O~
"""
from pytest import mark

import requests

_URL = 'http://localhost:8888'


@mark.gate0
def test_000_say_hello():
    """
    This is the 1st and simplest test of this game.
    You need to serve a server with /hello,
    which returns 'Hello world!' when GET.

    URL example: http://localhost:8888/hello
    """
    response = requests.get(_URL + '/hello')
    response.raise_for_status()
    assert response.content.decode() == 'Hello world!'
