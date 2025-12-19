from knot_hash import *


def main():
    # puzzle_input = 'flqrgnkx'
    puzzle_input = 'ugkiagan'
    disc_content = []

    for row_idx in range(128):
        input_str = f'{puzzle_input}-{row_idx}'
        input_length = [ord(c) for c in input_str]
        input_length.extend([17, 31, 73, 47, 23])
        numbers_list = list(range(256))
        k = KnotHash(numbers_list, input_length)

        for _ in range(64):
            k.knot_list()

        result_hash = ''
        for i in range(0, len(k.list), 16):
            block = k.list[i:i+16]
            xor_result = block[0]
            for number in block[1:]:
                xor_result = xor_result ^ number
            xor_hex = hex(xor_result)[2:]
            if len(xor_hex) == 1:
                xor_hex = '0' + xor_hex
            # print(xor_hex)
            result_hash += xor_hex

        results_binary = ''
        for digit in result_hash:
            integer = int(digit, 16)
            binary = format(integer, '0>4b')
            results_binary += binary
            # print(binary)
            # exit()
        results_binary = results_binary.replace('1', '#')
        results_binary = [char for char in results_binary]
        disc_content.append(results_binary)

    # for row in disc_content[:8]:
    #     print(row[:8])

    current_region = 1
    for i in range(128):
        for j in range(128):
            if check_point(disc_content, current_region, i, j):
                current_region += 1
    print(current_region-1)


def check_point(disc_content, current_region, i, j):
    if disc_content[i][j] != '#':
        return False
    disc_content[i][j] = f'{current_region}'
    for ni, nj in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
        if ni == -1 or ni == 128 or nj == -1 or nj == 128:
            continue
        check_point(disc_content, current_region, ni, nj)
    return True

    # n_used = 0
    # for row in disc_content:
    #     for bit in row:
    #         if bit == '1':
    #             n_used += 1
    # print(n_used)


if __name__ == '__main__':
    main()
