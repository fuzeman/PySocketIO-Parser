from pysocketio_parser.binary import deconstruct_packet, reconstruct_packet
import pysocketio_parser as parser
import helpers

from nose.tools import assert_equals


def test_deconstruct_string():
    assert_equals(deconstruct_packet({'nsp': '/', 'data': ['a', 1, {}], 'type': 3, 'id': 123}), {
        'packet': {
            'nsp': '/',
            'data': ['a', 1, {}],
            'type': 3,
            'id': 123,
            'attachments': 0
        },
        'buffers': []
    })


def test_deconstruct_bytearray():
    data = helpers.gen_bytearray()

    assert_equals(deconstruct_packet({
        'type': parser.BINARY_EVENT,
        'data': data,
        'id': 23,
        'nsp': '/cool'
    }), {
        'packet': {
            'type': parser.BINARY_EVENT,
            'data': {'_placeholder': True, 'num': 0},
            'id': 23,
            'nsp': '/cool',
            'attachments': 1
        },
        'buffers': [data]
    })


def test_encode_bytearray():
    helpers.test({
        'type': parser.BINARY_EVENT,
        'data': helpers.gen_bytearray(),
        'id': 23,
        'nsp': '/cool'
    })
