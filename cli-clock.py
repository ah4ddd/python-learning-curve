#!/usr/bin/env python3
import time
import datetime
import sys
import shutil
from colorama import init, Fore, Style
import pyfiglet

init(autoreset=True)

COLORS = [
    Fore.RED, Fore.GREEN, Fore.YELLOW,
    Fore.BLUE, Fore.MAGENTA, Fore.CYAN
]

def clear_screen():
    # Completely clear + move cursor to top-left
    sys.stdout.write("\033[2J\033[H")

def center(text, width):
    lines = text.split("\n")
    padded = []
    for line in lines:
        pad = max(0, (width - len(line)) // 2)
        padded.append(" " * pad + line)
    return "\n".join(padded)

while True:
    try:
        now = datetime.datetime.now()

        time_str = now.strftime("%H:%M:%S")
        date_str = now.strftime("%A, %d %B %Y")

        # Large ASCII text
        ascii_time = pyfiglet.figlet_format(time_str, font="big")

        # Color shift each second
        col = COLORS[now.second % len(COLORS)]
        colored_ascii_time = col + ascii_time + Style.RESET_ALL

        # Terminal size
        width = shutil.get_terminal_size().columns

        clear_screen()

        print(center(colored_ascii_time, width))
        print(center(Style.BRIGHT + date_str + Style.RESET_ALL, width))

        time.sleep(1)

    except KeyboardInterrupt:
        clear_screen()
        print("Clock terminated.")
        sys.exit(0)
