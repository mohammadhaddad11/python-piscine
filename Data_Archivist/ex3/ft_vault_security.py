def secure_archive(file: str, action: str = "r",
                   content: str = "") -> tuple[bool, str]:
    try:
        with open(file, action) as f:
            if action == "w":
                f.write(content)
                return (True, "Content successfully written to file")
            else:
                return (True, f.read())
    except FileNotFoundError as e:
        return (False, str(e))
    except PermissionError as e:
        return (False, str(e))
    except Exception as e:
        return (False, str(e))


if __name__ == "__main__":
    print("=== Cyber Archives Security ===\n")

    print("Using 'secure_archive' to read from a nonexistent file:")
    print(secure_archive("why.txt"))

    print("\nUsing 'secure_archive' to read from an inaccessible file:")
    print(secure_archive("/etc/master.passwd"))

    bol, cont = secure_archive("m.txt", "r")

    print("\nUsing 'secure_archive' to write previous content to a new file:")
    if bol:
        print(secure_archive("new.txt", "w", cont))
    else:
        print((False, cont))
