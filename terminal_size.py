"""Prints a 24 x 80 container to indicate terminal size"""


def display_terminal_size():

    print("-"*80)
    for i in range(23):
        print("|"+" "*78+"|")
    print("-"*80)


if __name__ == "__main__":
    display_terminal_size()
