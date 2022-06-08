from typing import Optional
from ctypes import wintypes , windll , create_unicode_buffer

def getForegroundWindow():
    hwnd = windll.user32.GetForegroundWindow()
    length = windll.user32.GetWindowTextLengthW(hwnd)
    buff = create_unicode_buffer(length + 1)
    windll.user32.GetWindowTextW(hwnd, buff, length + 1)
    if buff.value:
        return buff.value
    else:
        return None