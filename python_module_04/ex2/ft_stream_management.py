#!/usr/bin/env python3
import sys


def input_console(msg: str) -> str:
    sys.stdout.write("Input Stream active. ")
    txt = input(msg).strip()
    if not txt:
        raise ValueError
    else:
        return txt


def print_msg(msg: str, type="standard"):
    if type == "alert":
        sys.stderr.write("[ALERT] " + f"{msg}\n")
    elif type == "standard":
        sys.stdout.write("[STANDARD] " + f"{msg}\n")


def ft_stream_management():
    print("=== CYBER ARCHIVES - COMMUNICATION SYSTEM ===")
    try:
        archivist_id = input_console("Enter archivist ID: ")
    except ValueError:
        print()
        print_msg("System diagnostic: ID empty is not valid", "alert")
    else:
        try:
            status = input_console("Enter status report: ")
        except ValueError:
            print()
            print_msg("System diagnostic: Empty report is not valid", "alert")
        else:
            print()
            print_msg(f"Archive status from {archivist_id}: {status}")

            print_msg("System diagnostic: Communication channels verified",
                      "alert")

            print_msg("Data transmission complete")
            print()
            print("Three-channel communication test successful.")


ft_stream_management()
