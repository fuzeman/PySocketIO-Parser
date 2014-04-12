from threading import Event
import logging
import pysocketio_parser as parser

log = logging.getLogger(__name__)
encoder = parser.Encoder()


def test(obj):
    encode_event = Event()

    def callback(encodedPackets):
        log.debug('test callback - encodedPackets: %s', encodedPackets)
        decoder = parser.Decoder()
        decode_event = Event()

        @decoder.on('decoded')
        def decoded(packet):
            log.debug('test decoded - packet: %s', packet)

            assert packet == obj
            decode_event.set()

        decoder.add(encodedPackets[0])

        # Ensure decode fires
        assert decode_event.wait(3), "Decoder didn't return a result after 3 seconds"

        encode_event.set()

    encoder.encode(obj, callback)

    # Ensure encode fires
    assert encode_event.wait(3), "Encoder didn't return a result after 3 seconds"

