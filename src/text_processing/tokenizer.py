"""Streaming tokenization and word-frequency utilities.

This module tokenizes text files using ASCII alphanumeric characters,
normalizes tokens to lowercase, and computes word frequencies.
"""

import sys


def tokenize_stream(path: str):
    """Yield lowercase ASCII alphanumeric tokens from a text file.

    The file is read in chunks so that large files do not need to be
    loaded into memory at once.

    Runtime:
        O(N), where N is the number of characters in the file.
    """
    buffer = []

    with open(path, "r", encoding="utf-8", errors="ignore") as file:
        while True:
            chunk = file.read(4096)

            if not chunk:
                break

            for char in chunk:
                if char.isascii() and char.isalnum():
                    buffer.append(char.lower())

                elif char.isascii():
                    if buffer:
                        yield "".join(buffer)
                        buffer.clear()

                else:
                    # Ignore non-ASCII characters.
                    continue

    if buffer:
        yield "".join(buffer)


def tokenize(path: str) -> list[str]:
    """Return all tokens from a text file as a list.

    Runtime:
        O(T) time and O(T) space, where T is the number of tokens.
    """
    return list(tokenize_stream(path))


def compute_word_frequencies(tokens: list[str]) -> dict[str, int]:
    """Count the number of occurrences of each token.

    Runtime:
        O(T) expected time and O(U) space, where U is the number
        of unique tokens.
    """
    frequencies = {}

    for token in tokens:
        if token in frequencies:
            frequencies[token] += 1
        else:
            frequencies[token] = 1

    return frequencies


def print_frequencies(frequencies: dict[str, int]) -> None:
    """Print tokens by descending frequency and alphabetical order.

    Runtime:
        O(U log U), where U is the number of unique tokens.
    """
    items = list(frequencies.items())
    items.sort(key=lambda item: (-item[1], item[0]))

    for token, count in items:
        print(f"{token}\t{count}")


def main() -> None:
    """Run tokenization and frequency analysis from the command line."""
    try:
        args = sys.argv[1:]

        if len(args) != 1:
            print("Usage: python tokenizer.py <file>")
            sys.exit(1)

        tokens = tokenize(args[0])
        frequencies = compute_word_frequencies(tokens)
        print_frequencies(frequencies)

    except FileNotFoundError:
        print("Error: file not found")
        sys.exit(1)

    except PermissionError:
        print("Error: permission denied")
        sys.exit(1)

    except OSError:
        print("Error: unable to read file")
        sys.exit(1)


if __name__ == "__main__":
    main()
