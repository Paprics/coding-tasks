def sum_of_intervals(intervals: list[tuple[int, int]]) -> int:
    intervals = sorted(intervals)
    total = 0
    start, end = intervals[0]

    for i in range(1, len(intervals)):
        a, b = intervals[i]

        if a > end:
            total += end - start
            start, end = a, b
        elif a <= end and b > end:
            end = b

    total += end - start
    return total
