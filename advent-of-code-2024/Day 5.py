import re

def print_queue(input):
    # Variable to keep track of whether an update is allowed
    # And list to keep track of updates which are allowed
    correct = True
    correct_updates = []

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

                if after in update.split(","):
                    before_ind = update.split(",").index(before)
                    after_ind = update.split(",").index(after)
                    if after_ind < before_ind:
                        correct = False
        if correct:
            correct_updates.append(update.split(","))

    # Now get middle of each correct update and add to total
    total = 0
    for update in correct_updates:
        middle = ((len(update) + 1) / 2) - 1
        total += int(update[int(middle)])

    return total








puzzle_input = """"""

print(print_queue(puzzle_input))