#!/usr/bin/env python3
import sys


def ft_command_quest():
    print("=== Command Quest ===")
    n = len(sys.argv)
    if n == 1:
        print("No arguments provided!")
    print(f"Program name: {sys.argv[0]}")
    if n > 1:
        print(f"Arguments received: {n - 1}")
        for i in range(1, n):
            print(f"Argument {i}: {sys.argv[i]}")
    print(f"Total aruments: {n}")


# if __name__ == "__main__":
    # ft_command_quest()
