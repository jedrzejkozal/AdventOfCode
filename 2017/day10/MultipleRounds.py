from KnotHash import *

class MultipleRounds(object):
    def __init__(self):
        pass

    def convert_ASCII(self, string):
        converted = []

        for char in string:
            converted.append(ord(char))

        return converted

    def get_input_length(self, string):
        return self.convert_ASCII(string) + [17, 31, 73, 47, 23]

    def run_rounds(self):
        for i in range(64):
            self.knotHash.knot_list()
        return self.knotHash.list

    def dense_hash_block(self, sparse_hash):
        result = 0
        for i in range(len(sparse_hash)):
            result = result ^ sparse_hash[i]

        return result

    def dense_hash(self, input):
        block_len = 16
        result = []
        for i in range(0, len(input), block_len):
            result.append(self.dense_hash_block(input[i:i+block_len]))
        return result

    def calc_hash(self, list, input_ASCII):
        input = self.get_input_length(input_ASCII)
        self.knotHash = KnotHash(list, input)

        sparse = self.run_rounds()
        dense = self.dense_hash(sparse)
        return self.convert_to_hex(dense)

    def convert_to_hex(self, list):
        str = ""
        for number in list:
            str = str + hex(number)[2:]

        return str
