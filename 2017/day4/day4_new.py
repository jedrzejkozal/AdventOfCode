import collections


def main():
    passphrases_list: list[list[str]] = load_passphrases()

    n_valid = 0

    for passphrase in passphrases_list:
        if is_valid(passphrase):
            n_valid += 1

    print(n_valid)


def load_passphrases():
    with open('input_phase_two.txt', 'r') as f:
        file_content = f.read()
    file_content = file_content.split('\n')
    passphrases = [line.split(' ') for line in file_content]
    return passphrases


def is_valid(passphrase: list[str]):
    previous_counters = []

    for word in passphrase:
        word_counter = collections.Counter(word)
        for prev in previous_counters:
            if prev == word_counter:
                return False
        previous_counters.append(word_counter)

    return True


if __name__ == '__main__':
    main()
    # print(is_valid(['abcde', 'fghij']))
    # print(is_valid(['abcde', 'xyz', 'ecdab']))  # not
    # print(is_valid(['a', 'ab', 'abc', 'abd', 'abf', 'abj']))  # true
    # print(is_valid(['iiii', 'oiii', 'ooii', 'oooi', 'oooo']))  # true
    # print(is_valid(['oiii', 'ioii', 'iioi', 'iiio']))  # not valid
