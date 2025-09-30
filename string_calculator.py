def add(numbers: str) -> int:
    """Minimal implementation to pass the empty-string test."""
    if numbers == "":
        return 0
    # not implemented yet for other cases
    if "," not in numbers and "\n" not in numbers and not numbers.startswith("//"):
        return int(numbers)
    raise NotImplementedError("Not implemented yet")
