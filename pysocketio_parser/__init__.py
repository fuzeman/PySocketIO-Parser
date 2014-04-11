# Protocol version
PROTOCOL = 3

# Packet types.
TYPES = [
    'CONNECT',
    'DISCONNECT',
    'EVENT',
    'BINARY_EVENT',
    'ACK',
    'ERROR'
]

# Packet type `connect`.
CONNECT = 0

# Packet type `disconnect`.
DISCONNECT = 1

# Packet type `event`.
EVENT = 2

# Packet type `ack`.
ACK = 3

# Packet type `error`.
ERROR = 4

# Packet type `binary event`
BINARY_EVENT = 5


class Encoder(object):
    def __init__(self):
        """A socket.io Encoder instance"""
        pass

    def encode(self, obj, callback):
        """Encode a packet as a single string if non-binary, or as a
           buffer sequence, depending on packet type.

        :param obj: packet
        :type obj: dict

        :param callback: function to handle encodings (likely engine.write)
        :type callback: function

        :return: Calls callback with list of encodings
        """
        pass

    def string_encode(self, obj):
        """Encode packet as string.

        :param obj: packet
        :type obj: dict

        :return: encoded packet
        :rtype: str
        """
        pass

    def binary_encode(self, obj, callback):
        """Encode packet as 'buffer sequence' by removing blobs, and
           deconstructing packet into object with placeholders and
           a list of buffers.

        :param obj: packet
        :type obj: dict

        :return: encoded
        :rtype: bytearray
        """
        pass


class Decoder(object):
    def __init__(self):
        """A socket.io Decoder instance"""
        pass

    def add(self, obj):
        """Decodes an ecoded packet string into packet JSON.

        :param obj: encoded packet
        :type obj: str

        :return packet
        :rtype: dict
        """
        pass

    def destroy(self):
        """Deallocates a parser's resources"""
        pass


def string_decode(string):
    """Decode a packet String (JSON data)

    :param string: encoded packet string
    :type string: str

    :return: packet
    :rtype: dict
    """
    pass


class BinaryReconstructor(object):
    def __init__(self, packet):
        """A manager of a binary event's 'buffer sequence'. Should
           be constructed whenever a packet of type BINARY_EVENT is
           decoded.

        :param packet: packet
        :type packet: dict
        """
        pass

    def take_binary_data(self, bin_data):
        """Method to be called when binary data received from connection
           after a BINARY_EVENT packet.

        :param bin_data: the raw binary data received
        :type bin_data: bytearray

        :return: returns None if more binary data is expected or a
                 reconstructed packet object if all buffers have
                 been received
        :rtype: None or dict
        """
        pass

    def finished_reconstruction(self):
        """Cleans up binary packet reconstruction variables."""
        pass


def error(data):
    return {
        'type': ERROR,
        'data': 'parser error'
    }
