"""Module for parsing puzzle input."""


def read_file(absolute_path: str) -> list:
    """
    The function `read_file` reads the contents of a file named "input.txt" and returns them as a
    list of strings.
    :return: The function `read_file` returns a list of strings, where each string represents a line
    from the file "input.txt".
    """
    with open(file=f"{absolute_path}/input.txt", mode="r", encoding="UTF-8") as f:
        lines: list[str] = f.read().splitlines()

    return lines
