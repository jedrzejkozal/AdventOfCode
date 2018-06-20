import operator

class Registers(object):

    def __init__(self):
        self.dict = {}
        self.max_ever = 0

    def read_config(self):
        f = open("input.txt", 'r')
        table = []
        for elem in f:
            table.append(elem.split())
        return table

    def get_value_of_registers_od_add_them(self, string):
        try:
            value = self.dict[string]
        except KeyError:
            self.dict[string] = 0
            value = 0
        return value

    def set_register_value(self, string, val):
        self.dict[string] = val

    def get_value(self, string_list):
        register = self.get_value_of_registers_od_add_them(string_list[0])
        condition = self.get_value_of_registers_od_add_them(string_list[4])

        return register, condition

    def parse_comparator(self, string):
        if string == '<':
            return operator.__lt__
        elif string == '<=':
            return operator.__le__
        elif string == '>':
            return operator.__gt__
        elif string == '>=':
            return operator.__ge__
        elif string == '==':
            return operator.__eq__
        elif string == '!=':
            return operator.__ne__
        else:
            raise UnknownComparator

    def check_condition(self, register, comparator_string, number):
        cond = self.parse_comparator(comparator_string)
        return cond(register, number)

    def parse_operation(self, string):
        if string == 'inc':
            return operator.__add__
        elif string == 'dec':
            return operator.__sub__
        else:
            raise UnknownOperator

    def execute_operation(self, register, operation_string, number):
        operation = self.parse_operation(operation_string)
        return operation(register, number)

    def actualise_max(self):
        if self.dict[max(self.dict.iteritems(), key=operator.itemgetter(1))[0]] > self.max_ever:
            self.max_ever = self.dict[max(self.dict.iteritems(), key=operator.itemgetter(1))[0]]

    def parse_config(self):
        tab = self.read_config()

        for comand in tab:
            reg, cond = self.get_value(comand)
            if self.check_condition(cond, comand[5], int(comand[6])):
                new_val = self.execute_operation(reg, comand[1], int(comand[2]))
                #print new_val
                self.set_register_value(comand[0], new_val)
            self.actualise_max()

    def get_biggest_value(self):
        #return self.dict[max(self.dict)]
        return self.dict[max(self.dict.iteritems(), key=operator.itemgetter(1))[0]]

r = Registers()
#print r.read_config()
r.parse_config()
#print r.dict
print r.get_biggest_value()
print r.max_ever
