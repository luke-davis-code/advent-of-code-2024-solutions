import re

# PART ONE

def print_queue(input):
    # Variable to keep track of whether an update is allowed
    # And list to keep track of updates which are allowed
    correct = True
    total = 0

    split_inp = input.split("\n")
    sep_index = split_inp.index("")
    rules = " ".join(split_inp[:sep_index])
    updates = split_inp[sep_index + 1:]

    for update in updates:
        correct = True
        for num in update.split(","):
            this_num_rules = re.findall(r"%s\|\d+" % str(num), str(rules))
            for rule in this_num_rules:
                before = num
                after = rule[rule.index("|") + 1:]

                # Check if rule applys
                if after in update.split(","):
                    before_ind = update.split(",").index(before)
                    after_ind = update.split(",").index(after)
                    if after_ind < before_ind:
                        correct = False
        if correct:
            # Now get middle of each correct update and add to total
            middle = ((len(update.split(",")) + 1) / 2) - 1
            total += int(update.split(",")[int(middle)])

    return total

puzzle_input = """"""

print(print_queue(puzzle_input))

# PART TWO

# Use similar function to before

# First make a function that takes the incorrect inputs and fixes them using given rules
def sort_incorrect_update(update, rules):
    swaps = 0

    # Go through in reverse order
    # Sort list to the left of current item we are looking at
    correct_update = update.split(",")

    num_index = len(correct_update)-1
    while (num_index > 0):
        num = correct_update[num_index]
        this_num_rules = re.findall(r"%s\|\d+" % num, rules)

        for rule in this_num_rules:
            before = num
            after = rule[rule.index("|") + 1:]

            # Check if rule applies and needs correcting
            if after in correct_update:
                before_ind = correct_update.index(before)
                after_ind = correct_update.index(after)
                if after_ind < before_ind:
                    swaps += 1
                    # Swap them
                    temp = correct_update[after_ind]
                    correct_update[after_ind] = correct_update[before_ind]
                    correct_update[before_ind] = temp
                    print(correct_update)

        if swaps == 0:
            num_index -= 1
        swaps = 0

    return correct_update

def print_queue_II(input):
    # Variable to keep track of whether an update is allowed
    correct = True

    total = 0

    split_inp = input.split("\n")
    sep_index = split_inp.index("")
    rules = " ".join(split_inp[:sep_index])
    updates = split_inp[sep_index + 1:]

    for update in updates:
        correct = True
        for num in update.split(","):
            this_num_rules = re.findall(r"%s\|\d+" % num, rules)
            for rule in this_num_rules:
                before = num
                after = rule[rule.index("|") + 1:]

                # Check if rule applys
                if after in update.split(","):
                    before_ind = update.split(",").index(before)
                    after_ind = update.split(",").index(after)
                    if after_ind < before_ind:
                        correct = False
        # Edit so gives incorrect instead of correct
        if not correct:
            # Use sorting function and add the middle of this to total
            correct_update = sort_incorrect_update(update, rules)
            middle = ((len(correct_update) + 1) / 2) - 1
            total += int(correct_update[int(middle)])

    return total

print(print_queue_II(puzzle_input))