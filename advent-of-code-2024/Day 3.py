import re

# PART ONE

def get_valid_mul(memory):
    total = 0
    muls = re.findall(r"mul\(\d{1,3},\d{1,3}\)", memory)
    for mul in muls:
        nums = re.search(r"\d+,\d+", mul)
        a, b = nums.group().split(",")
        total += int(a) * int(b)

    return total

puzzle_input = """"""
print(get_valid_mul(puzzle_input))