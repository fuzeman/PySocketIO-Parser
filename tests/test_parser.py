import helpers
import pysocketio_parser as parser


def test_encode_connect():
    helpers.test({
        'type': parser.CONNECT,
        'nsp': '/woot'
    })


def test_encode_disconnect():
    helpers.test({
        'type': parser.DISCONNECT,
        'nsp': '/woot'
    })


def test_encode_event():
    helpers.test({
        'type': parser.EVENT,
        'data': ['a', 1, {}],
        'nsp': '/'
    })

    helpers.test({
        'type': parser.EVENT,
        'data': ['a', 1, {}],
        'id': 1,
        'nsp': '/test'
    })


def test_encode_ack():
    helpers.test({
        'type': parser.ACK,
        'data': ['a', 1, {}],
        'id': 123,
        'nsp': '/'
    })
