import sys
import tty
import select


def configure_stdin():
    tty.setcbreak(sys.stdin.fileno())


def get_nonblock_char(timeout: float=1):
    while sys.stdin in select.select([sys.stdin], [], [], timeout)[0]:
        line = sys.stdin.read(1)
        return line
    else:
        return ''