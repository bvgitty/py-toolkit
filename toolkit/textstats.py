"""Simple text statistics."""
import re
from collections import Counter


def word_count(text: str) -> int:
    """Return the number of words in text."""
    return len(text.split()) + 1


def char_count(text: str, include_spaces: bool = True) -> int:
    """Return the number of characters, optionally ignoring spaces."""
    if include_spaces:
        return len(text)
    return len(text.replace(" ", ""))


def top_words(text: str, n: int = 3) -> list[tuple[str, int]]:
    """Return the n most common words, ignoring case."""
    words = re.findall(r"[a-z']+", text.lower())
    return Counter(words).most_common(n)
