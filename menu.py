import os
import 
def main(options):
    index = 0
    while True:
        os.system('cls')
        for i, option in enumerate(options):
            prefix = "> " if i == index else "  "
            print(prefix + option)
        key = msvcrt.getch()
        if key in (b'\x00', b'\xe0'):
            key = msvcrt.getch()
        if key == b"H":
            index = (index - 1) % len(options)
        elif key == b"P":
            index = (index + 1) % len(options)
        elif key == b"\r":
            return index