import numpy as np


def main():
    filename = 'input.txt'
    # filename = 'input_test.txt'
    puzzle_input: list[str] = []
    with open(filename, 'r') as f:
        for line in f.readlines():
            puzzle_input.append(line)

    enhancement_rules_2: list[list[np.array]] = []
    enhancement_rules_3 = []
    for rule in puzzle_input:
        input_pattern, output_pattern = rule.replace(' ', '').split('=>')
        inp_rows = input_pattern.split('/')
        inp_rows = [list(row.replace('\n', '')) for row in inp_rows]
        img_input = np.array(inp_rows)
        out_rows = output_pattern.split('/')
        out_rows = [list(row.replace('\n', '')) for row in out_rows]
        img_output = np.array(out_rows)

        if img_input.shape[0] == 2:
            enhancement_rules_2.append([img_input, img_output])
        else:
            enhancement_rules_3.append([img_input, img_output])

    img_input = np.array([
        list('.#.'),
        list('..#'),
        list('###'),
    ])
    print(img_input)
    print()
    print()

    n_rounds = 5
    for _ in range(n_rounds):
        result_img = []
        if img_input.shape[0] % 2 == 0:
            for i in range(0, img_input.shape[0], 2):
                result_row = []
                for j in range(0, img_input.shape[1], 2):
                    sub_img = img_input[i:i+2, j:j+2]
                    for rule_inp, rule_out in enhancement_rules_2:
                        if np.unique(sub_img, return_counts=True)[1][0] != np.unique(rule_inp, return_counts=True)[1][0]:
                            continue

                        if match(rule_inp, sub_img):
                            result_row.append(rule_out)
                            break

                result_row = np.concatenate(result_row, axis=1)
                result_img.append(result_row)
        else:  # the case for 3x3 input img
            for i in range(0, img_input.shape[0], 3):
                result_row = []
                for j in range(0, img_input.shape[1], 3):
                    sub_img = img_input[i:i+3, j:j+3]
                    for rule_inp, rule_out in enhancement_rules_3:
                        if np.unique(sub_img, return_counts=True)[1][0] != np.unique(rule_inp, return_counts=True)[1][0]:
                            continue
                        # print(sub_img)
                        # print('---------------------------')
                        # print(rule_inp)
                        # print()
                        if match(rule_inp, sub_img):
                            result_row.append(rule_out)
                            break

                # print(result_row)
                result_row = np.concatenate(result_row, axis=1)
                result_img.append(result_row)

        result_img = np.concatenate(result_img, axis=0)
        img_input = result_img

    print(np.unique(img_input, return_counts=True))


def match(rule_inp, sub_img) -> bool:
    if (rule_inp == sub_img).all():
        return True
    if match_flips(rule_inp, sub_img):
        return True
    rule_inp = np.rot90(rule_inp)
    if (rule_inp == sub_img).all():
        return True
    if match_flips(rule_inp, sub_img):
        return True
    rule_inp = np.rot90(rule_inp)
    if (rule_inp == sub_img).all():
        return True
    if match_flips(rule_inp, sub_img):
        return True
    rule_inp = np.rot90(rule_inp)
    if (rule_inp == sub_img).all():
        return True
    if match_flips(rule_inp, sub_img):
        return True
    return False


def match_flips(rule_inp, sub_img):
    rule_inp = np.fliplr(rule_inp)
    if (rule_inp == sub_img).all():
        return True
    rule_inp = np.fliplr(rule_inp)
    rule_inp = np.flipud(rule_inp)
    if (rule_inp == sub_img).all():
        return True
    rule_inp = np.flipud(rule_inp)


if __name__ == '__main__':
    main()
