import collections


class Program:
    def __init__(self, program_id, second_program):
        self.registers = collections.defaultdict(int)
        self.registers['p'] = program_id
        self.queque = []
        self.second_program: Program = second_program
        self.wait_for_msg = False
        self.terminated = False
        self.instruction_idx = 0
        self.times_sent = 0

    def execute_instruction(self, instruction_list: list):
        instruction = instruction_list[self.instruction_idx]
        name = instruction[0]
        arg1 = instruction[1]
        if len(instruction) > 2:
            arg2 = instruction[2]

        if name == 'snd':
            value = santize_value(self.registers, arg1)
            self.second_program.queque.append(value)
            self.times_sent += 1
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
            if len(self.queque) == 0:
                self.wait_for_msg = True
                return
            else:
                self.registers[arg1] = self.queque.pop(0)
                self.wait_for_msg = False
        elif name == 'jgz':
            arg1 = santize_value(self.registers, arg1)
            if arg1 < 1:
                self.instruction_idx += 1
                # continue
                return
            arg2 = santize_value(self.registers, arg2)

            self.instruction_idx += arg2
            # continue
            return

        self.instruction_idx += 1

        if not 0 <= self.instruction_idx < len(instruction_list):
            self.terminated = True


def main():
    puzzle_input = []
    filename = 'input.txt'
    # filename = 'input_test1.txt'
    with open(filename, 'r') as f:
        for line in f.readlines():
            intruction = line.split()
            puzzle_input.append(intruction)

    program1 = Program(0, None)
    program2 = Program(1, None)
    program1.second_program = program2
    program2.second_program = program1
    while not (program1.terminated and program2.terminated):
        program1.execute_instruction(puzzle_input)
        program2.execute_instruction(puzzle_input)

        # print()
        # print(program1.registers)
        # print(program2.registers)

        if program1.wait_for_msg and program2.wait_for_msg:
            # print('break')
            break

    print(program2.times_sent)


def santize_value(registers, arg):
    return registers[arg] if 'a' <= arg <= 'z' else int(arg)


if __name__ == '__main__':
    main()
