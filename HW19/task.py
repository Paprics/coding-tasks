


def find_max_lake_depth(heights):
    n = len(heights)
    if n == 0:
        return 0

    left_max = [0] * n
    right_max = [0] * n

    left_peak = heights[0]
    for i in range(n):
        if heights[i] > left_peak:
            left_peak = heights[i]
        left_max[i] = left_peak

    right_peak = heights[-1]
    for i in range(n - 1, -1, -1):
        if heights[i] > right_peak:
            right_peak = heights[i]
        right_max[i] = right_peak

    max_depth = 0
    for i in range(n):
        water_level = min(left_max[i], right_max[i])
        depth_here = water_level - heights[i]
        if depth_here > max_depth:
            max_depth = depth_here

    return max_depth