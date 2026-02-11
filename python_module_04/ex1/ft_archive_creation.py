#!/usr/bin/env python3
def print_data(txt: str):
    """
    Read and display the entire content of a file-like object.

    :param txt: An open file object or stream to read from.
    """
    print("\nInscribing preservation data...")
    print(txt)


def create_archive(filename: str, txt: str):
    """
    Create a new storage file and write data to it using
    exclusive creation mode.

    :param filename: The name or path of the file to be created.
    :param txt: The string content to be written into the file.
    :raises FileExistsError: If the file already exists in the specified path.
    :return: The file created
    """
    print(f"Initializing new storage unit: {filename}")

    try:
        f = open(filename, "x")
    except FileExistsError:
        print("You are attempting to commit a crime,"
              f" the file \"{filename}\" already exists.")
    else:
        print("Storage unit created successfully...")
        try:
            f.write(txt)
        except Exception:
            print("Failed writing de data")
        else:
            print_data(txt)
            print("\nData inscription complete. Storage unit sealed.")
            print(f"Archive '{filename}' ready for long-term preservation.")
            return f


def ft_archive_creation():
    print("=== CYBER ARCHIVES - PRESERVATION SYSTEM ===")

    line1 = "{[}ENTRY 001{]} New quantum algorithm discovered\n"
    line2 = "{[}ENTRY 002{]} Efficiency increased by 347 %\n"
    line3 = "{[}ENTRY 003{]} Archived by Data Archivist trainee"

    f = create_archive("new_discovery.txt", line1 + line2 + line3)
    if f:
        f.close()


ft_archive_creation()
