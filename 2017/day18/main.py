import collections


class Program:
    def __init__(self):
        self.last_played_freq = None
        self.registers = collections.defaultdict(int)

    def execute(self, instruction_list: list):
        instruction_idx = 0
        while 0 <= instruction_idx < len(instruction_list):
            instruction = instruction_list[instruction_idx]
            name = instruction[0]
            arg1 = instruction[1]
            if len(instruction) > 2:
                arg2 = instruction[2]

            if name == 'snd':
                last_played_freq = self.registers[arg1]
            elif name == 'set':
                value = santize_value(self.registers, arg2)
                self.registers[arg1] = value
            elif name == 'add':
                value = santize_value(self.registers, arg2)
                self.registers[arg1] += value
            elif name == 'mul':
                value = santize_value(self.registers, arg2)
                self.registers[arg1] *= value
            elif name == 'mod':
                value = santize_value(self.registers, arg2)
                self.registers[arg1] %= value
            elif name == 'rcv':
                value = santize_value(self.registers, arg1)
                if value > 0:
                    print('recovered value = ', last_played_freq)
                    exit()
            elif name == 'jgz':
                arg1 = santize_value(self.registers, arg1)
                if arg1 < 1:
                    instruction_idx += 1
                    continue
                arg2 = santize_value(self.registers, arg2)

                instruction_idx += arg2
                continue

            instruction_idx += 1


def main():
    puzzle_input = []
    # filename = 'input_test.txt'
    filename = 'input.txt'
    with open(filename, 'r') as f:
        for line in f.readlines():
            intruction = line.split()
            puzzle_input.append(intruction)

    program = Program()
    program.execute(puzzle_input)


def santize_value(registers, arg):
    return registers[arg] if 'a' <= arg <= 'z' else int(arg)


if __name__ == '__main__':
    main()
