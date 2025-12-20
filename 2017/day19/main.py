

def main():
    # filename = 'input_test.txt'
    filename = 'input.txt'

    array: list[list[str]] = []
    with open(filename, 'r') as f:
        for line in f.readlines():
            array.append(line)

    # print(array)
    i, j = (0, array[0].index('|'))
    direction = 'down'
    current_char = array[i][j]

    collected_letters = []
    n_steps = 0

    while current_char != ' ':
        # update postion
        if direction == 'down':
            i += 1
        elif direction == 'up':
            i -= 1
        elif direction == 'left':
            j -= 1
        elif direction == 'right':
            j += 1

        # update direction
        current_char = array[i][j]
        if 'A' <= current_char <= 'Z':
            collected_letters.append(current_char)
        elif current_char == '+':
            if direction in ('up', 'down'):
                if array[i][j-1] != ' ':
                    direction = 'left'
                else:
                    direction = 'right'
            else:
                if array[i-1][j] != ' ':
                    direction = 'up'
                else:
                    direction = 'down'
        n_steps += 1

    # print(collected_letters)
    # print(('{}'*len(collected_letters)).format(*collected_letters))
    print(n_steps)


if __name__ == '__main__':
    main()
