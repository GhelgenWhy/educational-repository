"""word counter."""

import re


class EmptyTextError(ValueError):
    """exeption for empty text."""


def count_words(text: str) -> int:
    """count words in text.

    Args:
        text: str to analyze.

    Returns:
        amount of words in text.

    Raises:
        EmptyTextError: error if text is empty.
        TypeError: error if text is not string.

    Examples:
        >>> count_words("Hello world")
        2
        >>> count_words("Привіт, як справи?")
        3
        >>> count_words("one")
        1
        >>> count_words("  multiple   spaces   between  words  ")
        4
        >>> count_words("Line one\\nLine two\\nLine three")
        6
        >>> count_words("123 456 test")
        3
        >>> count_words("don't won't can't")
        3
        >>> count_words("")
        Traceback (most recent call last):
            ...
        word_counter.EmptyTextError: error if text is empty
        >>> count_words("   ")
        Traceback (most recent call last):
            ...
        word_counter.EmptyTextError: error if text is empty
        >>> count_words(None)
        Traceback (most recent call last):
            ...
        TypeError: expected str, got NoneType.
    """
    if not isinstance(text, str):
        raise TypeError(f"expected str, got {type(text).__name__}.")

    if not text.strip():
        raise EmptyTextError("error if text is empty")

    words = re.findall(r"\b[\w']+\b", text, flags=re.UNICODE)
    return len(words)


def main() -> None:
    """CLI entry point."""
    import sentry_config  # noqa: F401  pylint: disable=import-outside-toplevel,unused-import

    print("Enter text (Enter on empty line to finish):")
    lines = []
    try:
        while True:
            line = input()
            if line == "":
                break
            lines.append(line)
    except EOFError:
        pass

    text = "\n".join(lines)

    try:
        result = count_words(text)
        print(f"Amount of words: {result}")
    except EmptyTextError as exc:
        print(f"Error: {exc}")
        raise


if __name__ == "__main__":
    main()
