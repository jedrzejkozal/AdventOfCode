
class KnotHash(object):
    def __init__(self, list, input_length):
        self.list = list
        self.input_length = input_length
        self.current_position = 0
        self.skip_size = 0

    def knot_list(self):
        for inp_len in self.input_length:
            self.tie_knot(inp_len)

    def tie_knot(self, length):
        offset = self.current_position + length
        if offset < len(self.list):
            self.tie_normal(offset)
        else:
            self.tie_wrapped(offset)

        self.current_position += length + self.skip_size
        self.current_position %= len(self.list)
        self.skip_size += 1

    def tie_normal(self, offset):
        reverse = [e for e in reversed(self.list[self.current_position:offset])]
        self.list[self.current_position:offset] = reverse

    def tie_wrapped(self, offset):
        offset_wraped = offset - len(self.list)

        left_piece = self.list[0:offset_wraped]
        right_piece = self.list[self.current_position:len(self.list)]

        list_to_revert = right_piece + left_piece
        reverted_list = [e for e in reversed(list_to_revert)]

        left_reversed = reverted_list[0:len(right_piece)]
        right_reversed = reverted_list[len(right_piece):len(reverted_list)]

        self.list = right_reversed + self.list[offset_wraped:self.current_position] + left_reversed
