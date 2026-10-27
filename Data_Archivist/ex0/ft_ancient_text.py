import sys


def ft_ancient_text() -> None:
    if (len(sys.argv) != 2):
        print(f"Usage: {sys.argv[0]} <file>")
        return
    print(f"=== Cyber Archives Recovery ===\nAccessing file '{sys.argv[1]}'")

    f = None
    try:
        f = open(sys.argv[1], "r")
        content = f.read()
        print(f"---\n{content}\n---")
    except FileNotFoundError as e:
        print(f"Error opening file '{sys.argv[1]}': {e}")
    except PermissionError as e:
        print(f"Error opening file '{sys.argv[1]}': {e}")
    finally:
        if f is not None:
            print(f"File '{sys.argv[1]}' closed.")
            f.close()


if __name__ == "__main__":
    ft_ancient_text()
