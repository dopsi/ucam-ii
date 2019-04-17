def translate(cmd, name_only=False):
    r = "Unknown command"
    if len(cmd) != 6 or cmd[0] != 0xaa:
        r = "Error: invalid command (len={}, c={})".format(len(cmd), cmd)
    elif cmd[1] == 0x0e:
        r = "ACK"
        if not name_only:
            r += " for " + translate(bytes([0xaa, cmd[2], 0x00, 0x00, 0x00, 0x00]), name_only=True)
    elif cmd[1] == 0x0f:
        r = "NAK"
    elif cmd[1] == 0x01:
        r = "INITIAL"
    elif cmd[1] == 0x05:
        r = "SNAPSHOT"
    elif cmd[1] == 0x04:
        r = "GET PICTURE"
    elif cmd[1] == 0x0a:
        r = "DATA"

    return r


def sync():
    return bytes([0xaa, 0x0d, 0x00, 0x00, 0x00, 0x00])


def ack(cmd):
    return bytes([0xaa, 0x0e, cmd[1], 0x00, 0x00, 0x00])


def initial():
    return bytes([0xAA, 0x01, 0x00, 0x03, 0x01, 0x00])


def snapshot():
    return bytes([0xAA, 0x05, 0x01, 0x00, 0x00, 0x00])


def get_picture():
    return bytes([0xAA, 0x04, 0x01, 0x00, 0x00, 0x00])
