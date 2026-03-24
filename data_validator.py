"""Data validation utilities for structured records."""


def validate_email(email):
    """Check if a string looks like a valid email address."""
    if not isinstance(email, str):
        return False
    if not email:
        return False
    parts = email.split("@")
    if len(parts) != 2:
        return False
    local, domain = parts
    if not local or not domain:
        return False
    if "." not in domain:
        return False
    return True


def validate_age(age):
    """Validate that age is a reasonable integer value."""
    if isinstance(age, bool) or not isinstance(age, int):
        raise TypeError("age must be an integer")
    if age < 0 or age > 150:
        raise ValueError("age must be between 0 and 150")
    return True


def validate_record(record):
    """Validate a user record dictionary.

    Expected keys: name, email, age
    Returns a list of validation errors (empty list = valid).
    """
    if not isinstance(record, dict):
        return ["record must be a dict"]
    errors = []

    if "name" not in record:
        errors.append("missing required field: name")
    elif not isinstance(record["name"], str) or len(record["name"]) == 0:
        errors.append("name must be a non-empty string")

    if "email" not in record:
        errors.append("missing required field: email")
    elif not validate_email(record["email"]):
        errors.append("invalid email format")

    if "age" not in record:
        errors.append("missing required field: age")
    else:
        try:
            validate_age(record["age"])
        except (TypeError, ValueError) as e:
            errors.append(str(e))

    return errors


def normalize_name(name):
    """Normalize a name by stripping whitespace and title-casing."""
    if not isinstance(name, str):
        raise TypeError("name must be a string")
    return name.strip().title()


def batch_validate(records):
    """Validate a list of records and return results.

    Returns a dict mapping index to list of errors.
    Only includes records that have errors.
    """
    if not isinstance(records, list):
        raise TypeError("records must be a list")
    results = {}
    for i, record in enumerate(records):
        errors = validate_record(record)
        if errors:
            results[i] = errors
    return results
