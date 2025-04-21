from enum import Enum

RESET = "\033[0m"

class Color(Enum):
    RED = "\033[91m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    BLUE = "\033[94m"
    MAGENTA = "\033[95m"
    CYAN = "\033[96m"
    WHITE = "\033[97m"
    BLACK = "\033[90m"
    BRIGHT_RED = "\033[91;1m"
    BRIGHT_GREEN = "\033[92;1m"
    BRIGHT_YELLOW = "\033[93;1m"
    BRIGHT_BLUE = "\033[94;1m"
    BRIGHT_MAGENTA = "\033[95;1m"
    BRIGHT_CYAN = "\033[96;1m"
    BRIGHT_WHITE = "\033[97;1m"

def print_colored(text: str, color: Color):
    print(f"{color.value}{text}{RESET}")
