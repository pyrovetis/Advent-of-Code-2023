"""Day 1 of advent of code 2023."""

import os
import re
from typing import Any, Generator

from utils.pprint import pprint
from utils.read_file import read_file

DIGITS = {
    "zero": 0,
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}


def get_numbers(lines: list[str]) -> Generator[int, Any, None]:
    _ = []
    for line in lines:
        for character in line[:]:
            if character.isdigit():
                _.append(int(character))
        yield _
        _.clear()


def get_numbers_two(lines: list[str]) -> Generator[int, Any, None]:
    _ = []
    for line in lines:
        _ = ["#"] * len(line)
        
        for item in DIGITS.values():
            for occurrences in [m.start() for m in re.finditer(str(item), line)]:
                _[occurrences] = item

        for item in DIGITS:
            for occurrences in [m.start() for m in re.finditer(item, line)]:
                _[occurrences] = DIGITS.get(item)
                print(
                    f"occurrences: {occurrences: <10}",
                    f"item: {item: <10}",
                    f"line: {line: <10}",
                    f"value: {[value for value in _ if value != "#"]}",
                )
        yield [value for value in _ if value != "#"]
        _.clear()


def parse_numbers(lines: list[int]) -> Generator[int, Any, None]:
    for line in lines:
        yield int(f"{line[0]}{line[-1]}")


def part_one() -> None:
    lines = read_file(os.path.dirname(__file__))
    numbers = get_numbers(lines)
    result = sum(parse_numbers(numbers))

    pprint(result)


def part_two() -> None:
    lines = read_file(os.path.dirname(__file__))
    numbers = get_numbers_two(lines)
    result = sum(parse_numbers(numbers))

    pprint(result, 2)


def main():
    part_one()
    part_two()


if __name__ == "__main__":
    main()
