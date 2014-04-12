from threading import Event
import logging
import pysocketio_parser as parser

log = logging.getLogger(__name__)
encoder = parser.Encoder()


def test(obj):
    encode_event = Event()

    def callback(encoded_packets):
        log.debug('test callback - encoded_packets: %s', encoded_packets)
        decoder = parser.Decoder()
        decode_event = Event()

        @decoder.on('decoded')
        def decoded(packet):
            log.debug('test decoded - packet: %s', packet)

            assert packet == obj
            decode_event.set()

        for ep in encoded_packets:
            decoder.add(ep)

        # Ensure decode fires
        assert decode_event.wait(3), "Decoder didn't return a result after 3 seconds"

        encode_event.set()

    encoder.encode(obj, callback)

    # Ensure encode fires
    assert encode_event.wait(3), "Encoder didn't return a result after 3 seconds"


def gen_string(size=5, start=0):
    return ''.join([chr(x) for x in range(start, start + size)])


def gen_bytearray(size=5, start=0):
    return bytearray(gen_string(size, start))
