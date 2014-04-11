from threading import Event
import logging
import pysocketio_parser as parser

log = logging.getLogger(__name__)
encoder = parser.Encoder()


def test(obj):
    def callback(encodedPackets):
        log.debug('test callback - encodedPackets: %s', encodedPackets)
        decoder = parser.Decoder()
        event = Event()

        @decoder.on('decoded')
        def decoded(packet):
            log.debug('test decoded - packet: %s', packet)

            assert packet == obj
            event.set()

        decoder.add(encodedPackets[0])
        assert event.wait(5)

    encoder.encode(obj, callback)
