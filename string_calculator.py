def add(numbers: str) -> int:
    """Minimal implementation to pass the empty-string test."""
    if numbers == "":
        return 0
    
    if numbers.startswith("//"):
        raise NotImplementedError("Custom delimiter not implemented yet")
    
    if "\n" in numbers:
        raise NotImplementedError("Newline support not implemented yet")
    # not implemented yet for other cases
    parts = numbers.split(",")
    return sum(int(p) for p in parts if p != "")
