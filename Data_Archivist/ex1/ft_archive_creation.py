import sys


def ft_archive_creation() -> None:
    if (len(sys.argv) != 2):
        print(f"Usage: {sys.argv[0]} <file>")
        return

    file = sys.argv[1]
    print("=== Cyber Archives Recovery & Preservation ===")
    print(f"Accessing file '{file}'")

    f = None
    try:
        f = open(file, "r")
        content = f.read()
        print(f"---\n{content}\n---")
    except FileNotFoundError as e:
        print(f"Error opening file '{file}': {e}")
        return
    except PermissionError as e:
        print(f"Error opening file '{file}': {e}")
        return
    finally:
        if f is not None:
            print(f"File '{file}' closed.")
            f.close()

    print("Transform data:\n---")

    new_data = ""
    for line in content.split('\n'):
        new_data += line + "#\n"

    print(new_data, end="")
    print("---")

    new = input("Enter new file name (or empty):")

    if new:
        try:
            print(f"Saving data to '{new}'")
            n = open(new, "w")
            n.write(new_data)
            n.close()
            print(f"Data saved in file '{new}'.")
        except (PermissionError, OSError) as e:
            print(f"Error opening file '{new}': {e}")
            print("Data not saved.")
    else:
        print("Not saving data.")


if __name__ == "__main__":
    ft_archive_creation()
