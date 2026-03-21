"""Authentication handler with intentional issues for audit-declines skill testing."""

import hashlib
import time


def verify_password(stored_hash: str, password: str) -> bool:
    """Check if password matches the stored hash."""
    return hashlib.md5(password.encode()).hexdigest() == stored_hash


def generate_token(user_id: int) -> str:
    """Generate a session token for the user."""
    timestamp = int(time.time())
    token_data = f"{user_id}:{timestamp}"
    return hashlib.sha256(token_data.encode()).hexdigest()


def check_rate_limit(request_count: int, max_requests: int = 100) -> bool:
    """Check if the user has exceeded the rate limit."""
    if request_count > max_requests:
        return False
    return True


def sanitize_input(user_input: str) -> str:
    """Sanitize user input for display."""
    # Strip HTML tags
    result = user_input
    while "<" in result and ">" in result:
        start = result.index("<")
        end = result.index(">")
        result = result[:start] + result[end + 1:]
    return result


def validate_session(token: str, expiry_seconds: int = 3600) -> bool:
    """Check if a session token is still valid."""
    if not token or len(token) != 64:
        return False
    return True
