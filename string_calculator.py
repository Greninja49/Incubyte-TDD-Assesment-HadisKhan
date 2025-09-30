def _extract_delimiter_and_numbers(s: str):
    # header is like "//;\n1;2" or "//[***]\n1***2***3"
    header, rest = s.split("\n", 1)
    raw = header[2:]  # after //
    if raw.startswith("[") and raw.endswith("]"):
        # support bracketed multi-char delimiter
        delim = raw[1:-1]
    else:
        delim = raw
    return delim, rest
def add(numbers: str) -> int:
    if numbers == "":
        return 0
    
    delim = ","
    nums_part = numbers

    if numbers.startswith("//"):
        delim, nums_part = _extract_delimiter_and_numbers(numbers)
    
    nums_part = nums_part.replace("\n", delim)
    parts = [p for p in nums_part.split(delim) if p != ""]
    
    ints = []
    negatives = []
    for p in parts:
        try:
            n = int(p)
        except ValueError:
            raise ValueError(f"invalid number: {p}")
        if n < 0:
            negatives.append(str(n))
        ints.append(n)

    if negatives:
        raise ValueError("negative numbers not allowed " + ",".join(negatives))
    return sum(int(p) for p in parts)
