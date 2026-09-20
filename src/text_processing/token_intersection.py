"""Memory-aware token intersection for two text files.

This module counts the number of unique tokens shared by two files.
It stores tokens from the smaller file in memory and streams through
the larger file to reduce memory usage.
"""

import os
import sys

from tokenizer import tokenize_stream


def count_common_tokens(path1: str, path2: str) -> int:
    """Return the number of unique tokens shared by two files.

    The smaller file is selected using file size. Its tokens are stored
    in a set, while the larger file is processed as a stream.

    Runtime:
        O(N1 + N2) expected time, where N1 and N2 are the numbers of
        characters processed from the two files.

    Space:
        O(U_small + U_common), where U_small is the number of unique
        tokens in the smaller file and U_common is the number of unique
        tokens shared by both files.
    """
    size1 = os.path.getsize(path1)
    size2 = os.path.getsize(path2)

    if size1 <= size2:
        smaller_path, larger_path = path1, path2
    else:
        smaller_path, larger_path = path2, path1

    smaller_tokens = set(tokenize_stream(smaller_path))
    common_tokens = set()

    for token in tokenize_stream(larger_path):
        if token in smaller_tokens:
            common_tokens.add(token)

    return len(common_tokens)


def main() -> None:
    """Count shared unique tokens between two command-line input files."""
    try:
        args = sys.argv[1:]

        if len(args) != 2:
            print(
                "Usage: python token_intersection.py <file1> <file2>"
            )
            sys.exit(1)

        result = count_common_tokens(args[0], args[1])
        print(result)

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
