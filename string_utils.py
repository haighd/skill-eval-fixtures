def is_palindrome(text: str) -> bool:
    """Return True if text is a palindrome, ignoring spaces and case."""
    cleaned = text.replace(" ", "").lower()
    return cleaned == cleaned[::-1]


def char_frequency(text: str) -> dict:
    """Return a dictionary of character frequencies in text."""
    freq = {}
    for char in text:
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1
    return freq


def word_count(text: str) -> int:
    """Return the number of words in text."""
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    if text == "":
        raise ValueError("text must not be empty")
    return len(text.split())


def truncate(text: str, max_length: int) -> str:
    """Truncate text to max_length characters, appending '...' if truncated.

    Note: Truncation operates on raw text including any leading/trailing whitespace.
    """
    if max_length <= 0:
        raise ValueError("max_length must be a positive integer")
    if len(text) <= max_length:
        return text
    return text[:max_length] + "..."
