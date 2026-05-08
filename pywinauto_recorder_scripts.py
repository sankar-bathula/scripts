import os
import time

from pywinauto_recorder.recorder import *

# Open Notepad
os.system("start notepad")

# Wait for app to open
time.sleep(2)

# Type text
send_keys("hello shankar")

# Optional: press enter
send_keys("{ENTER}")

# More text
send_keys("Automation using pywinauto_recorder")