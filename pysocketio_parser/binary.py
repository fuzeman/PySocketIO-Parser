import logging

log = logging.getLogger(__name__)


def deconstruct_packet(packet):
    buffers = []
    p_data = packet['data']

    def deconstruct(data):
        if not data:
            return data

        if type(data) is bytearray:
            placeholder = {'_placeholder': True, 'num': len(buffers)}
            buffers.append(data)
            return placeholder
        elif type(data) is list:
            return [deconstruct(item) for item in data]
        elif type(data) is dict:
            return dict([(key, deconstruct(value)) for key, value in data.items()])

        return data

    pack = packet
    pack['data'] = deconstruct(p_data)
    pack['attachments'] = len(buffers)

    return {
        'packet': pack,
        'buffers': buffers
    }


def reconstruct_packet(packet, buffers):
    log.debug("reconstruct_packet packet: %s, buffers: %s", repr(packet), repr(buffers))

    def reconstruct(data):
        log.debug("reconstruct data: %s", repr(data))

        if data and data.get('_placeholder'):
            buf = buffers[data['num']]
            return buf
        elif type(data) is list:
            return [reconstruct(item) for item in data]
        elif type(data) is dict:
            return dict([(key, reconstruct(value)) for key, value in data])

        return data

    packet['data'] = reconstruct(packet['data'])

    del packet['attachments']

    return packet
