import collections
import time
from tqdm import tqdm
from copy import deepcopy


def dance(input_str, string):
    sequence = input_str.split(',')

    intermediate_results = []
    intermediate_results.append(deepcopy(string))

    for move_idx, move in enumerate(sequence):
        if move[0] == 's':
            string = spin(move[1:], string)
        elif move[0] == 'x':
            exchange(move[1:], string)
        elif move[0] == 'p':
            partner(move[1:], string)

        if string in intermediate_results:
            i = intermediate_results.index(string)
            print(f'found repeated move: {move} at indexes: {move_idx+1}: {string} and {i}: {intermediate_results[i]}')
        intermediate_results.append(deepcopy(string))
    return string


def spin(X, string):
    index = int(X)
    return string[-index:] + string[:-index]


def exchange(AB, string):
    A, B = AB.split('/')
    swapAB(string, int(A), int(B))


def partner(AB, string: list):
    A, B = AB.split('/')
    A_index = find(string, A)
    B_index = find(string, B)
    swapAB(string, A_index, B_index)


def swapAB(string, A, B):
    string[A], string[B] = string[B], string[A]


def find(some_list, token):
    for index, l in enumerate(some_list):
        if l == token:
            return index


if __name__ == '__main__':
    f = open('input.txt')
    input = f.read()
    f.close()

    string = "a b c d e f g h i j k l m n o p".split()
    # string = "l m n o p a b c d e f g h i j k".split()

    # for _ in tqdm(range(1000000000), total=1000000000):
    # for _ in range(1000000000):
    #     output = dance(input, string)
    #     string = output
    # print(output)
    # exit()

    n = 1000000  # 1000 * 10000 / 600000 = 16.66
    string = "a b c d e f g h i j k l m n o p".split()
    sequence = input.split(',')

    # intermediate_results = []
    # intermediate_results.append(deepcopy(string))
    # already_reapeated = []
    counter = collections.defaultdict(int)
    previous_occurece = collections.defaultdict(list)

    cycle_started = False

    move_idx = 0
    for _ in range(n):
        for move in sequence:
            if move[0] == 's':
                string = spin(move[1:], string)
            elif move[0] == 'x':
                exchange(move[1:], string)
            elif move[0] == 'p':
                partner(move[1:], string)

            string_str = ('{}'*16).format(*string)
            counter[string_str] += 1
            previous_occurece[string_str].append(move_idx)
            diff = [prev_idx - previous_occurece[string_str][i] for i, prev_idx in enumerate(previous_occurece[string_str][1:])]
            if counter[string_str] > 100 and diff[0] < max(diff):  # and all([diff[i] == diff[0] for i in range(len(diff))]):
                print()
                print(f'cycle found at move {move_idx}, string = {string}')  # prev occurences = {previous_occurece[string_str]}')
                print(diff)

            # if string == ['p', 'i', 'h', 'g', 'l', 'b', 'f', 'a', 'c', 'j', 'm', 'k', 'e', 'n', 'd', 'o']:
            #     print(move_idx)
            #     # results:
            #     # ['i', 'e', 'j', 'f', 'd', 'l', 'h', 'c', 'm', 'b', 'p', 'k', 'g', 'o', 'n', 'a']:  104174
            #     # ['d', 'a', 'o', 'c', 'j', 'p', 'g', 'k', 'e', 'h', 'f', 'b', 'l', 'n', 'm', 'i']:  120774
            #     # ['p', 'i', 'h', 'g', 'l', 'b', 'f', 'a', 'c', 'j', 'm', 'k', 'e', 'n', 'd', 'o']:  212180

            #     exit()

            if move_idx == 399999:  # 400001:
                string_str = ('{}'*16).format(*string)
                print('answer = ', string_str)
                exit()

            # if string in intermediate_results:
            #     i = intermediate_results.index(string)
            #     if move_idx - i < 100:
            #         move_idx += 1
            #         continue
            #     # print()
            #     # print(f'found repeated move: {move} at indexes: {move_idx+1} and {i}')
            #     # print(string)
            #     # print(intermediate_results[i])
            #     already_reapeated.append(deepcopy(string))
            #     if string in already_reapeated:
            #         j = already_reapeated.index(string)
            #         print(f'found repeated move: {move} at indexes: {move_idx+1} and {i} {j}')
            #         print(string)
            #         string_str = ('{}'*16).format(*string)
            #         print(string_str)
            #         print(already_reapeated[j])
            # intermediate_results.append(deepcopy(string))
            move_idx += 1

    out = ""
    for s in string:
        out += s

    print(out)  # result for n: 1000 = gnflbkojhicpmead
    # gnflbkojhicpmead
    # gnflbkojhicpmead
    # assert out == 'ociedpjbmfnkhlga'
