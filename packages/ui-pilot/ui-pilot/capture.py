import cv2
from cv2 import VideoWriter, VideoWriter_fourcc

from PIL import ImageGrab

import pyscreeze
import PIL
# HACK
__PIL_TUPLE_VERSION = tuple(int(x) for x in PIL.__version__.split('.'))
pyscreeze.PIL__version__ = __PIL_TUPLE_VERSION

import pyautogui as pg
import numpy as np
import time
import os

from mss import mss

from pynput import keyboard, mouse



def save_screenshot():
    time.sleep(2)
    screenshot = cv2.cvtColor(np.array(pg.screenshot()), cv2.COLOR_RGB2BGR)

    # cv2.imshow('screenshot', screenshot)
    imagepath = os.path.join(
        os.path.expanduser("~/Desktop"),
        "screenshot.png"
    )
    cv2.imwrite(imagepath, screenshot)

    # cv2.waitKey(0)

    cv2.destroyAllWindows()


def save_video():
    fps = 3 # due to slow screenshot
    delay = 1 / fps
    size = (1440, 900)
    video = VideoWriter(
        'test.avi',
        VideoWriter_fourcc(*'MJPG'),
        fps,
        frameSize=size,
    )

    def main():
        while True:
            start = time.time()
            # with mss() as sct:
            #     filename = sct.shot()
            # raw_screenshot = cv2.imread(filename) # 0.2s
            # raw_screenshot = pg.screenshot() # 0.3s
            raw_screenshot = ImageGrab.grab() # 0.5s
            print(time.time() - start)
            pixels = np.array(raw_screenshot)
            image = cv2.resize(pixels, size)
            screenshot = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

            video.write(screenshot)

            key = cv2.waitKey(int(delay * 1000))
            if key & 0xFF == 27: break


        video.release()
        cv2.destroyAllWindows()

    main()


def capture_keyboard():
    def on_press(key):
        print(key)

    listener = keyboard.Listener(on_press=on_press)
    listener.start()

    while True:
        time.sleep(1)


# https://pypi.org/project/pynput
def capture_mouse():
    def on_move(x, y):
        print('Pointer moved to {0}'.format(
            (x, y)))

    def on_click(x, y, button, pressed):
        print('{0} at {1}'.format(
            'Pressed' if pressed else 'Released',
            (x, y)))
        # if not pressed:
        #     # Stop listener
        #     return False

    def on_scroll(x, y, dx, dy):
        print('Scrolled {0} at {1}'.format(
            'down' if dy < 0 else 'up',
            (x, y)))

    listener = mouse.Listener(
        on_move=on_move,
        on_click=on_click,
        on_scroll=on_scroll
    )
    listener.start()

    while True:
        time.sleep(1)


if __name__ == '__main__':
    # save_video()
    # capture_keyboard()
    capture_mouse()
