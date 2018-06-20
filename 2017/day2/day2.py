

class SpreadsheetReader:
    def __init__(self):
        self.filename = "input.txt"

    def read(self):
        f = open(self.filename, 'r')
        table = []
        for elem in f:
            read = [int(s) for s in elem.split() if s.isdigit()]
            table.append(read)

        return table

class ChecksumDiffCalculator:

    def find_min_and_max(self, numbers):
        max = 0
        min = float('inf')
        for i in numbers:
            if i > max:
                max = i
            if i < min:
                min = i

        return min, max

    def calculate_row_diffrence(self, numbers):
        min, max = self.find_min_and_max(numbers)
        return max - min

    def calculate_checksum_diffrence(self, array):
        sum = 0
        for e in array:
            sum += self.calculate_row_diffrence(e)

        return sum

class ChecksumDivCalculator:

    def divide(self, a, b):
        if a < b:
            return b / a
        else:
            return a / b

    def check_if_are_divisable(self, a, b):
        if a < b:
            return b % a == 0
        else:
            return a % b == 0

    def find_two_divisable_numbers(self, numbers):
        for i in numbers:
            for j in numbers:
                if i != j and self.check_if_are_divisable(i,j):
                    return i, j

    def calculate_row_div(self, numbers):
        i, j = self.find_two_divisable_numbers(numbers)
        return self.divide(i, j)

    def calculate_checksum_div(self, array):
        sum = 0
        for e in array:
            sum += self.calculate_row_div(e)

        return sum

if __name__ == "__main__":
    r = SpreadsheetReader()
    array = r.read()

    #c = ChecksumDiffCalculator()
    #print c.calculate_checksum_diffrence(array)

    c = ChecksumDivCalculator()
    print c.calculate_checksum_div(array)
