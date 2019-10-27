import time


def dance(input_str, string):
    sequence = input_str.split(',')

    s_time, x_time, p_time = 0.0, 0.0, 0.0

    for move in sequence:
        if move[0] == 's':
            t0 = time.time()
            string = spin(move[1:], string)
            s_time += time.time() - t0
        elif move[0] == 'x':
            t0 = time.time()
            exchange(move[1:], string)
            x_time += time.time() - t0
        elif move[0] == 'p':
            t0 = time.time()
            partner(move[1:], string)
            p_time += time.time() - t0
    return string, s_time, x_time, p_time


def spin(X, string):
    index = int(X)
    return string[-index:] + string[:-index]


def exchange(AB, string):
    A, B = AB.split('/')
    swapAB(string, int(A), int(B))


def partner(AB, string):
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

    # for _ in range(1000000000):
    #     output = dance(input, string)
    #     string = output
    # print(output)

    s_avrg_time, x_avrg_time, p_avrg_time = 0.0, 0.0, 0.0
    n = 1000
    for _ in range(n):
        string = "a b c d e f g h i j k l m n o p".split()
        output, s_time, x_time, p_time = dance(input, string)
        s_avrg_time += s_time
        x_avrg_time += x_time
        p_avrg_time += p_time
    print("elapsed times = {}, {}, {}".format(s_avrg_time/n,
                                              x_avrg_time/n,
                                              p_avrg_time/n))

    out = ""
    for s in output:
        out += s

    print(out)
    assert out == 'ociedpjbmfnkhlga'
