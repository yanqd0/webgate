"""
This is just a beginning.
Enjoy the journey O(∩_∩)O~
"""
from pytest import mark

import requests

from . import URL


@mark.gate00
def test_000_say_hello():
    """
    This is the 1st and simplest test of this game.
    You need to start a server with /hello,
    which returns 'Hello world!' when GET.

    After you cross the gate, you know how to serve at least.

    URL example: http://localhost:8888/hello
    """
    response = requests.get(URL + '/hello')
    response.raise_for_status()
    assert response.content.decode() == 'Hello world!'
