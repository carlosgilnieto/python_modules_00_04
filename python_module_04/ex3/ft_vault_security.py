#!/usr/bin/env python3

def secure_extraction(file: str) -> None:
    """
    Perform a safe read operation on a specified file using a context manager.

    :param file: The path to the file to be read and displayed.
    :raises FileNotFoundError: If the path of the file is not the correct,
                               prevent the read of the file
    """
    print("\nSECURE EXTRACTION:")
    try:
        with open(file) as f:
            return f.read()
    except FileNotFoundError:
        return "[ALERT] Vault connection failed..."


def secure_preservation(file: str, msg: str) -> None:
    """
    Safely create a new file and write a message to it using
    exclusive creation mode.

    :param file: The path where the new file will be created.
    :param msg: The string content to be written and displayed.
    :raises FileExistsError: If the file already exists, preventing data
                             overwrite.
    """
    print("\nSECURE PRESERVATION:")
    try:
        with open(file, "x") as f:
            f.write(msg)
            print(msg)
    except FileExistsError:
        print("[ALERT] Fail preserving the archive...")


def ft_vault_security():
    print("=== CYBER ARCHIVES - VAULT SECURITY SYSTEM ===\n")

    print("Initiating secure vault access...")
    print("Vault connection established with failsafe protocols")

    txt = secure_extraction("classified_data.txt")
    print(txt)

    msg = "[CLASSIFIED] New security protocols archived"
    secure_preservation("new_archive.txt", msg)

    print("Vault automatically sealed upon completion")

    print("\nAll vault operations completed with maximum security.")


ft_vault_security()
