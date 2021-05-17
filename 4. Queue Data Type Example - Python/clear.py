import os
import platform
platform = platform.system()
if platform == 'Darwin':
    clear = "clear"
elif platform == 'Windows':
    clear = 'cls'


def clear():
    os.system(clear)