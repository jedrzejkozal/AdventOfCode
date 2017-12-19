class CaptchaSolver:

    def solve_using_next(self, string):
        sum = 0

        for i in range(len(string)):
            #print string[i], string[i+self.offset]
            if string[i] == string[(i+1) % len(string)]:
                sum += int(string[i])

        return sum

    def solve_using_halfway(self, string):
        offset = len(string)/2
        sum = 0

        for i in range(len(string)/2):
            #print string[i], string[i+self.offset]
            if string[i] == string[(i+offset) % len(string)]:
                sum += int(string[i])*2

        return sum
