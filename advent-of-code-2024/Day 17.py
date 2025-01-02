import math

# Make an object to represent the computer (seemed best way to handle this problem)
class ChronoComputer:
    def __init__(self, inp_program, inp_A, inp_B, inp_C):
        self.program = inp_program

        self.initialA = inp_A
        self.initialB = inp_B
        self.initialC = inp_C

        self.A = inp_A
        self.B = inp_B
        self.C = inp_C

        self.instruction_pointer = 0
        self.jumped = False

        self.output = []

    def get_combo(self, operand):
        if 0 <= operand <= 3:
            return operand
        if operand == 4:
            return self.A
        if operand == 5:
            return self.B
        if operand == 6:
            return self.C
        # 7 is reserved and does not appear in valid programs

    def adv(self, operand):
        numerator = self.A
        denominator = 2**(self.get_combo(operand))
        # set A register to truncated division
        self.A = math.trunc(numerator / denominator)

    def bxl(self, operand):
        bitwise_xor = self.B ^ operand
        self.B = bitwise_xor

    def bst(self, operand):
        modulo = self.get_combo(operand) % 8
        self.B = modulo

    def jnz(self, operand):
        if self.A != 0:
            self.instruction_pointer = operand
            self.jumped = True

    def bxc(self, operand):
        bitwise_xor = self.B ^ self.C
        self.B = bitwise_xor

    def out(self, operand):
        output_value = self.get_combo(operand) % 8
        return output_value

    def bdv(self, operand):
        numerator = self.A
        denominator = 2 ** (self.get_combo(operand))
        # set B register to truncated division
        self.B = math.trunc(numerator / denominator)

    def cdv(self, operand):
        numerator = self.A
        denominator = 2 ** (self.get_combo(operand))
        # set A register to truncated division
        self.C = math.trunc(numerator / denominator)

    def run_program(self):
        while self.instruction_pointer < len(self.program):
            opcode = self.program[self.instruction_pointer]
            operand = self.program[self.instruction_pointer+1]

            if opcode == 0:
                self.adv(operand)
            elif opcode == 1:
                self.bxl(operand)
            elif opcode == 2:
                self.bst(operand)
            elif opcode == 3:
                self.jnz(operand)
            elif opcode == 4:
                self.bxc(operand)
            elif opcode == 5:
                self.output.append(self.out(operand))
            elif opcode == 6:
                self.bdv(operand)
            elif opcode == 7:
                self.cdv(operand)

            if not self.jumped:
                self.instruction_pointer += 2
            self.jumped = False

    def reset(self):
        self.A = self.initialA
        self.B = self.initialB
        self.C = self.initialC
        self.instruction_pointer = 0
        self.jumped = False
        self.output = []

    def set_A(self, new_A):
        self.A = new_A


puzzle_input = """Register A: 47792830
Register B: 0
Register C: 0

Program: 2,4,1,5,7,5,1,6,4,3,5,5,0,3,3,0
"""

# PART ONE

# Parse puzzle input to seperate
lines = puzzle_input.split("\n")
initial_A = int(lines[0].split(":")[1])
initial_B = int(lines[1].split(":")[1])
initial_C = int(lines[2].split(":")[1])
program = [int(num) for num in lines[4].split(":")[1].split(",")]

# Make a new chrono computer object
chrono = ChronoComputer(program, initial_A, initial_B, initial_C)

chrono.run_program()

# Get part one output from this
answer = ""
for i in range(len(chrono.output)):
    if i == len(chrono.output) - 1:
        answer += str(chrono.output[i])
    else:
        answer += str(chrono.output[i])
        answer += ","

print(answer)

# PART TWO
#
# trial_a = 0
# while program != chrono.output:
#     trial_a += 1
#     chrono.reset()
#     chrono.set_A(trial_a)
#     chrono.run_program()
# print(trial_a)







