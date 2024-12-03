import numpy as np

# PART ONE

def get_safe_count(data):
    safe_count = 0

    reports = data.split("\n")

    for report in reports:
        levels = [int(n) for n in report.split(" ")]
        diff_list = np.diff(levels)
        print(diff_list)

        if all(1 <= x < 4 for x in diff_list) or all(-4 < x <= -1 for x in diff_list):
            safe_count += 1

    print(safe_count)

puzzle_input = """Put input here ...
"""
print(get_safe_count(puzzle_input))

# PART TWO



