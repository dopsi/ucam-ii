from time import sleep

from serial import Serial

from PIL import Image

from ucam_ii import synchronize, take_picture

if __name__ == '__main__':
    ser = Serial('/dev/ttyUSB0')
    synchronize(ser)
    i = 0
    while True:
        i = i + 1
        sleep(2)
        raw = take_picture(ser)
        img = Image.frombytes('P', (80, 60), raw)
        img.show()
        img.save("img-{}.bmp".format(i))
