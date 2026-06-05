
def divide (a:int, b:int) -> float:
    return a/b

def safe_divide(a:int, b:int) -> float:
    try:
        return divide(a, b)
    except ZeroDivisionError:
        return float('inf')

def parse_size(size: str) -> int:
    """Parse a size string like '10K', '5M', '2G' into bytes.

    K=1024, M=1024**2, G=1024**3, T=1024**4.
    Raises:
        TypeError: if `size` is not a str.
        ValueError: if `size` is empty, has an unknown unit suffix,
            has a non-numeric magnitude, or is negative.
    """
    _UNITS = {"K": 1024, "M": 1024 ** 2, "G": 1024 ** 3, "T": 1024 ** 4}
    if not isinstance(size, str):
        raise TypeError(f"size must be str, got {type(size).__name__}")
    size = size.strip()
    if not size:
        raise ValueError("empty size string")

    last = size[-1]
    if last.isalpha():
        if last not in _UNITS:
            raise ValueError(f"unknown unit: {last!r}")
        magnitude, multiplier = size[:-1], _UNITS[last]
    else:
        magnitude, multiplier = size, 1

    try:
        value = int(magnitude)
    except ValueError as e:
        raise ValueError(f"invalid number: {magnitude!r}") from e

    if value < 0:
        raise ValueError(f"negative size not allowed: {value}")

    return value * multiplier
