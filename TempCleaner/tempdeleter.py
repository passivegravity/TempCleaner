# -*- coding: utf-8 -*-
# Copyright (C) 2023 https://github.com/LowOnGravity
#
# This source code has been released under the GNU Affero General Public
# License v3.0. A copy of this license is available at
# https://www.gnu.org/licenses/agpl-3.0.en.html


import os
import shutil
from colorama import Fore, Style
import art
import termcolor

# Define colors
HEADER_COLOR = Fore.LIGHTMAGENTA_EX
WARNING_COLOR = Fore.YELLOW
CLEANING_COLOR = Fore.MAGENTA
SUCCESS_COLOR = Fore.MAGENTA + Style.BRIGHT
FREED_COLOR = Fore.CYAN
ERROR_COLOR = Fore.RED
RESET_COLOR = Style.RESET_ALL
CREATOR_COLOR = Fore.MAGENTA + Style.BRIGHT
CONSOLE_COLOR = Fore.CYAN

# Custom purple gradient color definition
def purple(text):
    os.system("")
    faded = ""
    down = False

    for line in text.splitlines():
        red = 40
        for character in line:
            if down:
                red -= 3
            else:
                red += 3
            if red > 254:
                red = 254
                down = True
            elif red < 1:
                red = 1
                down = False
            faded += (f"\033[38;2;{red};0;220m{character}\033[0m")
        faded += "\n"
    return faded


# Set the title of the Command Prompt window
os.system("title Temp Cleaner")

# Print header
header = purple(art.text2art("Cleaner"))
print(CONSOLE_COLOR + header)

# Print creator info
print(CREATOR_COLOR + "Developed by Simon\n\n" + RESET_COLOR)

 # Changing this does not make you a developer of any sort.

folders = [
    os.path.join(os.environ["SYSTEMDRIVE"], "Windows", "Temp"),
    os.path.join(os.environ["USERPROFILE"], "AppData", "Local", "Temp")
]

total_freed = 0

for folder in folders:
    print(CLEANING_COLOR + f"[ {CONSOLE_COLOR}CONSOLE{CLEANING_COLOR} ] Cleaning up " +  folder + RESET_COLOR)
    try:
        freed = 0
        for root, dirs, files in os.walk(folder):
            for file in files:
                try:
                    path = os.path.join(root, file)
                    size = os.path.getsize(path)
                    os.remove(path)
                    freed += size
                except Exception as e:
                    pass
        if isinstance(freed, int):
            total_freed += freed
            print(SUCCESS_COLOR + f"[ {CONSOLE_COLOR}CONSOLE{SUCCESS_COLOR} ] Cleaned up {FREED_COLOR}{freed / 1024 / 1024:.2f} MB" + SUCCESS_COLOR + f" in {folder}" + RESET_COLOR)
        else:
            pass
    except Exception as e:
        pass

print("\n" + SUCCESS_COLOR + f"[ {CONSOLE_COLOR}CONSOLE{SUCCESS_COLOR} ] Total space freed: {FREED_COLOR}{total_freed / 1024 / 1024:.2f} MB" + RESET_COLOR)

input("Press Enter to exit...")  # Add this line to prevent console window from closing immediately
