def add(numbers: str) -> int:
    """Minimal implementation to pass the empty-string test."""
    if numbers == "":
        return 0
    
    if numbers.startswith("//"):
        raise NotImplementedError("Custom delimiter not implemented yet")
    
    normalized = numbers.replace("\n", ",")
    parts = [p for p in normalized.split(",") if p != ""]
    return sum(int(p) for p in parts)
