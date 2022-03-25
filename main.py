# Python实用宝典
# 2022-03-25
import time
import win32gui
from PIL import ImageGrab


def get_window_pos(name):
    name = name
    handle = win32gui.FindWindow(0, name)
    if handle == 0:
        return None
    else:
        return win32gui.GetWindowRect(handle), handle

while True:
    try:
        (x1, y1, x2, y2), handle = get_window_pos('极限竞速：地平线 4')
        win32gui.SetForegroundWindow(handle)
        img_ready = ImageGrab.grab((x1, y1, x2, y2))
        img_ready.save(f"./result/{time.time()}.jpg")
        time.sleep(5)
    except Exception as e:
        print(e)