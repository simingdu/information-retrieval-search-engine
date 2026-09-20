"""Content filtering utilities for web crawling.

These helpers identify oversized responses and low-information pages
before they are accepted into a crawl.
"""


DEFAULT_MAX_PAGE_SIZE = 5_000_000
DEFAULT_MIN_CONTENT_TOKENS = 50


def exceeds_size_limit(
    html: bytes,
    content_length: str | None = None,
    max_bytes: int = DEFAULT_MAX_PAGE_SIZE,
) -> bool:
    """Return True when a page exceeds the configured size limit.

    Content-Length is checked first when available. The raw HTML size is
    also checked as a fallback when the header is missing or unreliable.
    """
    if content_length and content_length.isdigit():
        if int(content_length) > max_bytes:
            return True

    return len(html) > max_bytes


def is_low_information(
    filtered_tokens: list[str],
    min_tokens: int = DEFAULT_MIN_CONTENT_TOKENS,
) -> bool:
    """Return True when a page contains too few meaningful tokens."""
    return len(filtered_tokens) < min_tokens
