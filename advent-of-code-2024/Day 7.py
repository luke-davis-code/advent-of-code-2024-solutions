import itertools

# PART ONE

def parser(numbers, operator_combination):
    # Output starts as first number
    total = int(numbers[0])

    number_next = True
    current_num = 0
    i = 1
    j = 0
    while i < len(numbers) or j < len(operator_combination):
        if number_next:
            current_num = numbers[i]
            i += 1
            number_next = False
        else:
            if operator_combination[j] == '+':
                total += int(current_num)
            else:
                total *= int(current_num)
            j += 1
            number_next = True

    return total


def calibration(equation_input):
    total = 0

    equations = equation_input.split("\n")
    for i in range(len(equations)):
        equations[i] = equations[i].split(": ")

    for equation in equations:
        correct = False
        test_value = equation[0]
        nums = equation[1].split(" ")

        operator_count = len(nums) - 1

        # Use itertools to get all ways the operators can be arranged
        possible_ways = [way for way in itertools.product(["+", "*"], repeat=operator_count)]

        for way in possible_ways:
            if parser(nums, way) == int(test_value):
                correct = True

        if correct:
            total += int(test_value)

    return total

puzzle_input = """"""

print(calibration(puzzle_input))