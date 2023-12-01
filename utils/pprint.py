"""Module for printing results."""

PART_ONE_TEXT = (
    "# ─── Part one ───────────────────────────────────────────────────────────── ✣ ─"
)
PART_TWO_TEXT = (
    "# ─── Part two ───────────────────────────────────────────────────────────── ✣ ─"
)


def pprint(solution: str, part: int = 1) -> None:
    """
    The `pprint` function prints the solution and a text based on the part number.

    :param solution: The `solution` parameter is a string that represents the solution to a problem or
    task. It is the output that you want to print
    :type solution: str
    :param part: The `part` parameter is an optional integer that specifies which part of the solution
    to print. If `part` is set to 1, it will print the solution for part one. If `part` is set to any
    other value, it will print the solution for part two, defaults to 1
    :type part: int (optional)
    """
    if part == 1:
        print(PART_ONE_TEXT)
    else:
        print(PART_TWO_TEXT)

    print(solution)
