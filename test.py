# This will be a working python script someday
def normalize_number(
    num: int, rmin: int, rmax: int, tmin: int, tmax: int) -> int:
    """
    Apply linear normalization to the input number, to scale
    it down to the new range. In order to compensate the fact
    that close input numbers will give the same result,
    the function adds the last digit of the input number to
    the final result.
    num: Number to scale down
    rmin:  Lowest possible number in source range
    rmax:  Highest possible number in source range
    tmin:  Lowest possible number in target range
    tmax:  Highest possible number in target range
    Returns the input number scaled down to the new range.

    If the input number is lower than 255, do not normalize.
    """
    if not num:
        return 0
    if num < 255:
        return num

    linear_normalization = int(round((float(num - rmin) / float(rmax - rmin)) * (tmax - tmin) + tmin))

    if linear_normalization + (num % 10) > 255:
        linear_normalization = linear_normalization - 255 + (num % 10)
    else:
        linear_normalization = linear_normalization + num % 10
    return linear_normalization

result = normalize_number(600, 1, 4096, 200, 255)
print(result)
