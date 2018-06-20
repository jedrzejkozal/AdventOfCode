

class StreamProcessor(object):

    def __init__(self):
        self.groups = ""
        self.string = ""
        self.removed_chars = 0

    def read_input(self):
        f = open("input.txt", 'r')
        self.string = f.read()
        f.close()

    def remove_char_from_string(self, string, index):
        return string[0:index] + string[index+1:len(string)]

    def clean_garbage(self, string):
        isGarbage = False
        i = 0
        self.removed_chars = 0

        while i < len(string):
            if string[i] == '!':
                string = self.remove_char_from_string(string, i)
                string = self.remove_char_from_string(string, i)
            elif string[i] == '>':
                string = self.remove_char_from_string(string, i)
                isGarbage = False
            elif isGarbage:
                self.removed_chars += 1
                string = self.remove_char_from_string(string, i)
            elif string[i] == '<':
                string = self.remove_char_from_string(string, i)
                isGarbage = True
            else:
                i += 1
        return string

    def count_score(self, string):
        string = self.clean_garbage(string)

        actual_score = 0
        overall_score = 0

        for char in string:
            if char == '{':
                actual_score += 1
            elif char == '}':
                overall_score += actual_score
                actual_score -= 1
            elif char == ',' or '\n':
                continue
            else:
                print ">%c<" % char
                raise Exception('StringNotClearedProperly')

        return overall_score

if __name__ == '__main__':
    s = StreamProcessor()
    s.read_input()
    s.clean_garbage(s.string)
    print s.count_score(s.string)
    print s.removed_chars
