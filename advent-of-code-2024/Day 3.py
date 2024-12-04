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

# PART TWO

def get_valid_mul_II(memory, do_flag=True, total=0):

    # Find next don't (as default is do)
    # Do everything up to that don't (keep track in total)
    # Now look for next do
    # Ignore everything up to that do
    # REPEAT ... until either no more dos to find or no more dont's

    # Base case(s)
    if re.search(r"do\(\)|don't\(\)", memory) is None:
        if do_flag:
            total += get_valid_mul(memory)
        return total

    else:
        # Recursive case
        if do_flag:
            dontpos = re.search(r"don't\(\)", memory)
            if dontpos is None:
                return total + get_valid_mul(memory)
            total += get_valid_mul(memory[:dontpos.end()])
            do_flag = False
            return get_valid_mul_II(memory[dontpos.end():], do_flag, total)
        else:
            dopos = re.search(r"do\(\)", memory)
            if dopos is None:
                return total
            do_flag = True
            return get_valid_mul_II(memory[dopos.end():], do_flag, total)

print(get_valid_mul_II(puzzle_input))