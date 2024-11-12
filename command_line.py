import sys
from typing import Optional

if __name__ == '__main__':
    print(sys.argv)
def str_to_float(s: str) -> Optional[float]:
    try:
        return float(s)
    except ValueError:
        return None

def sum_command_line_args(args: list[str]) -> float:
    total = 0.0
    for arg in args:
        number = str_to_float(arg)
        if number is not None:
            total += number
    return total

if __name__ == "__main__":
    args = sys.argv[1:]
    total_sum = sum_command_line_args(args)
    print("The sum of the command-line arguments is:", total_sum)

#Command input  == command_line.py 3.14 abc 2.71 5.0 xyz

