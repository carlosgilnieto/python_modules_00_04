#!/usr/bin/env python3
def print_data(txt):
    """
    Read and display the entire content of a file-like object.

    :param txt: An open file object or stream to read from.
    """
    print("\nRECOVERY DATA:")
    print(txt.read())


def storage_vault(dir: str) -> None:
    """
    Open a data file, display its content using an external function,
    and manage the connection.

    :param dir: The file system path to the storage vault file.
    :raises FileNotFoundError: If the specified directory or
            file does not exist.
    """
    print(f"\nAccessing Storage Vault: {dir}")

    try:
        txt = open(dir)
    except FileNotFoundError:
        print("ERROR: Storage vault not found. Run data generator first.")
    else:
        print("Connection established...")
        print_data(txt)
        print("\nData recovery complete. Storage unit disconnected.")
        txt.close()


def ft_ancient_text():
    print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===")
    storage_vault("ancient_fragmen.txt")


ft_ancient_text()
