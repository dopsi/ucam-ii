from serial import Serial

from ucam_ii.command import ack, get_picture, initial, snapshot, sync, translate


def synchronize(ser: Serial):
    timeout = 0.020
    while True:
        cmd = sync()
        ser.write(cmd)
        ser.timeout = timeout
        r = ser.read(6)
        timeout += 0.005

        print("W:{} R:{}".format(translate(cmd), translate(r)))

        if len(r) == 6 and r[1] == 0xe:
            break

    r = ser.read(6)
    cmd = ack(r)
    ser.write(cmd)

    print("R:{} W:{}".format(translate(r), translate(cmd)))


def take_picture(ser: Serial):
    for cmd in [initial(), snapshot(), get_picture()]:
        ser.write(cmd)
        r = bytes()
        while len(r) < 6:
            r += ser.read(1)
        print("W:{} R:{}".format(translate(cmd), translate(r)))

    r = bytes()
    while len(r) < (6 + 60 * 80):
        r += ser.read(1)

    print(r)

    cmd = ack(bytes([0xaa, 0x0a, 0x00, 0x00, 0x00, 0x00]))
    ser.write(cmd)

    print("R:{} W:{}".format(translate(r[0:6]), translate(cmd)))

    print(r)

    return bytes(r[6:])
