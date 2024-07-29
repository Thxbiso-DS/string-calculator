import re


def check_consecutive_delimiters(numbers: str, delimiter: str) -> None:
    delimiter_length = len(delimiter)
    for position in range(len(numbers) - delimiter_length):
        current_slice = numbers[position : position + delimiter_length]
        next_slice = numbers[position + 1 : position + 1 + delimiter_length]
        if current_slice == next_slice == delimiter:
            raise ValueError("ERROR: invalid input")


def extract_delimiter_and_numbers(string_int: str) -> tuple[list[str], str]:
    if string_int.startswith("//"):
        match = re.match(r"//(.+)\n(.+)", string_int, re.DOTALL)
        if match:
            delimiters, numbers = match.groups()

            if delimiters.startswith("[") and delimiters.endswith("]"):
                delimiters = re.findall(r"\[(.*?)\]", delimiters)
                if any(
                    "[" in delimiter or "]" in delimiter for delimiter in delimiters
                ):
                    raise ValueError("ERROR: invalid input")
            else:
                if "[" in delimiters or "]" in delimiters:
                    raise ValueError("ERROR: invalid input")
                delimiters = [delimiters]

            for delimiter in delimiters:
                if numbers.startswith(delimiter) or numbers.endswith(delimiter):
                    raise ValueError("ERROR: invalid input")

                check_consecutive_delimiters(numbers, delimiter)

            return delimiters, numbers

        return [string_int[2]], ""
    return [","], string_int


def parse_numbers(numbers: str, delimiters: list[str]) -> list[int]:
    if not numbers:
        return []

    delimiter_pattern = "|".join(map(re.escape, delimiters))
    return [int(num) for num in re.split(rf"{delimiter_pattern}|\n", numbers) if num]


def handle_negative_integers(integers: list[int]) -> None:
    negative_integers = [num for num in integers if num < 0]
    if negative_integers:
        raise ValueError(
            f"negatives not allowed: {', '.join(map(str, negative_integers))}"
        )


def add(string_int: str) -> int:
    if not isinstance(string_int, str):
        raise TypeError("The numbers of the function argument must be a string")

    if not string_int:
        return 0

    delimiters, numbers = extract_delimiter_and_numbers(string_int)
    integers = parse_numbers(numbers, delimiters)
    handle_negative_integers(integers)

    integers = [number for number in integers if number < 1000]

    return sum(integers)
