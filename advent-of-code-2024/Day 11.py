# PART ONE

# Use a list of strings to represent the stones

def remove_extra_zeroes(num_string):
    # Remove unecessary leading zeros
    i = 0
    while i < len(num_string)-1 and num_string[i] == "0":
        i += 1
    return num_string[i:]

def blink(stones):
    new_stones = ["" for _ in range(len(stones))]
    # Pointer for position in old list
    i = 0
    # Pointer for position in new list
    j = 0
    while i < len(stones):
        # Go through rules until find first applicable
        if stones[i] == "0":
            new_stones[j] = "1"
            i += 1
            j += 1
        elif len(stones[i]) % 2 == 0:
            middle = int(len(stones[i]) / 2)
            # Get stones and remove any leading zeros
            stone1 = remove_extra_zeroes(stones[i][:middle])
            stone2 = remove_extra_zeroes(stones[i][middle:])

            # Add both to new stones list
            # First increase length of list by 1 (add extra empty)
            new_stones.append("")
            new_stones[j] = stone1
            new_stones[j+1] = stone2
            i += 1
            j += 2
        else:
            new_stones[j] = str(int(stones[i]) * 2024)
            i += 1
            j += 1

    return new_stones

puzzle_input = "6 11 33023 4134 564 0 8922422 688775"
stones = puzzle_input.split(" ")
num_blinks = 25
for i in range(num_blinks):
    stones = blink(stones)
print(len(stones))

