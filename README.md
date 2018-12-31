# WebGate

[![License](https://img.shields.io/github/license/yanqd0/webgate.svg)](https://github.com/yanqd0/webgate/blob/master/LICENSE)

This is a TDD tutorial (or a game) of the basic web programming.

Come and pass tests, cross the gate one by one, you will become a web developer.

## Prepare Environment

Python 2 or 3 (recommended) with `pip` is required.

```sh
pip install pytest requests
```

## Pass Tests

After your server is started, make sure it listens to the port `8888`.
Read the test cases in `tests/test_*.py`, and learn from error messages.

Try to pass all the tests:

```sh
pytest
```

Of course, this is not a good move for newbies.
You are going to be inundated by error messages.
Please take small steps forward.

### Gate by gate

It is not so easy to passing all tests.
You can cross it one by one.

```sh
pytest -m gate00
# or
pytest -m gate01
# more
pytest -m gate00,gate01
```

The gates:

- `gate00`: Run a server, return `Hello world!`.
- `gate01`: 3 simple ways to handle the arguments from clients.
- `gate02`: Receive and return with JSON.

`pydoc` can provide more information, like:

```sh
pydoc tests.test_gate00
```

### Case by case

You can see the name of test cases in `pytest`.
You can run it alone with its name.

```sh
pytest tests/test_gate01.py::test_002_gender
# or with parameters
pytest tests/test_gate01.py::test_002_gender[Alice-Female]
```

## Recommendations

It is recommended to fork this repository,
then create branches named as `flask`, `django` and so on to keep your implementations.

It is tested in Python, but implementations could be any framework in any language.

A pull request is welcome if you have any idea about this repository.

### Language

There are some programming languages for newbies:

- **[Python]**
- [Golang]
- [JavaScript]
- [Kotlin]
- [Ruby]

[Python]:https://www.python.org/
[Golang]:https://golang.org/
[Kotlin]:https://kotlinlang.org/
[Ruby]:https://www.ruby-lang.org/
[JavaScript]:https://www.javascript.com/

### Frameworks

There are some web frameworks for newbies:

- **[Flask]**
- [Django]
- **[Node.js]**

[Flask] is used when test cases are developing.

[Flask]:http://flask.pocoo.org/
[Django]:https://djangoproject.com/
[Falcon]:https://falconframework.org/
[Node.js]:https://nodejs.org/
