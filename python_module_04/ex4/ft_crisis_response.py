#!/usr/bin/env python3

def crisis_handler(fn: str, msg: str) -> None:
    """
    Attempt to recover data from a file while managing potential access or
    system errors.

    :param fn: The filename or path of the archive to access.
    :param msg: A custom message to display at the start of the recovery
                attempt.
    """
    print(f"\n{msg}: Attempting access to '{fn}'...")

    try:
        with open(fn) as f:
            txt = f.read()
            print(f"SUCCESS: Archive recovered - ``{txt}''")
            print("STATUS: Normal operations resumed")
    except FileNotFoundError:
        print("RESPONSE: Archive not found in storage matrix")
        print("STATUS: Crisis handled, system stable")
    except PermissionError:
        print("RESPONSE: Security protocols deny access")
        print("STATUS: Crisis handled, security maintained")
    except Exception:
        print("RESPONSE: Unexpected system anomaly")
        print("STATUS: Crisis handled, emergency protocols active")


def ft_crisis_response():
    print("=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===")

    crisis_handler("lost_archive.txt", "CRISIS ALERT")
    crisis_handler("classified_vault.txt", "CRISIS ALERT")
    crisis_handler("standard_archive.txt", "ROUTINE ACCESS")

    print("\nAll crisis scenearios handled successfully. Archives secure.")


ft_crisis_response()
