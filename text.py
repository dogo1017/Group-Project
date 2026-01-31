def bubble(string, width=100):
    import time
    import sys
    import textwrap
    lines = textwrap.wrap(string, width - 4)
    print(f"/{ '-' * (width - 2) }\\")

    for _ in lines:
        print(f"| {' ' * (width - 4)} |")
    print(f"\\{ '-' * (width - 2) }/")
    sys.stdout.write(f"\033[{len(lines) + 1}A")

    for line in lines:
        sys.stdout.write("\033[2C")
        for char in line:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.04)
        sys.stdout.write("\n")
    sys.stdout.write("\033[1B\r") 

# HOW TO USE:
# you literally just input a string in the function while calling it and it makes it look fancy

def credits():
    pass