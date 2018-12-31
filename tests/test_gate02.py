"""
JSON is the most popular way to transmit messages in web.
You need to handle it in this gate.
"""
import math
import random

import requests
from pytest import mark

from . import URL


@mark.gate02
@mark.parametrize(
    'operator, num0, num1, result',
    [
        ('+', 2, 1, 3),
        ('+', random.randint(-127, 128), random.randint(-127, 128), None),
        ('-', 2, 1, 1),
        ('-', random.randint(-127, 128), random.randint(-127, 128), None),
        ('*', 2, 1, 2),
        ('*', random.randint(-127, 128), random.randint(-127, 128), None),
        ('/', 2, 1, 2),
        ('/', random.randint(-127, 128), random.randint(-127, 128), None),
    ]
)
def test_005_calc(operator, num0, num1, result):
    """
    This case requires a simple calculator in the web.
    You need to receive and handle JSON, and return results with JSON.

    URL example: http://localhost:8888/calc
    """
    response = requests.post(
        URL + '/calc',
        json=dict(
            operator=operator,
            num0=num0,
            num1=num1,
        ),
    )
    response.raise_for_status()
    if result is None:
        # Never use `eval` in a server!
        # pylint: disable=eval-used
        result = eval('{}{}{}'.format(num0, operator, num1))
    assert result == response.json().get('result')


@mark.gate02
def test_006_calc_div0():
    """
    Handle errors when the divisor is 0.

    URL example: http://localhost:8888/calc
    """
    response = requests.post(
        URL + '/calc',
        json=dict(
            operator='/',
            num0=1,
            num1=0,
        ),
    )
    assert math.isnan(response.json().get('result'))
