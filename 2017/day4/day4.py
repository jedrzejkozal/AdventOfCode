
class PassphraseContains(object):

    def __init__(self):
        self.map = {}

    def add(self, letter):
        try:
            self.map[letter] = self.map[letter]+1
        except(KeyError):
            self.map[letter] = 1


class Passphrase(object):
    def __init__(self):
        self.validPass = 0

    def read_line(self):
        f = open('input.txt','r')
        for l in f:
            yield l

    def get_list_from_line(self):
        for line in self.read_line():
            yield line.split()
            #print words

    def has_duplicates(self, list):
        return len(list) == len(set(list))

    def iterate_all(self):
        for list in self.get_list_from_line():
            if self.has_duplicates(list):
                self.validPass += 1

    def from_word_get_dictiony(self, word):
        pc = PassphraseContains()
        for letter in word:
            pc.add(letter)
        return pc.map

    def get_list_of_maps(self, list):
        maps = []
        for elem in list:
            maps.append(self.from_word_get_dictiony(elem))
        #print maps
        return maps

    def dictionaries_are_same(self, dic1, dic2):
        shared_items = set(dic1.items()) & set(dic2.items())
        return len(shared_items) == len(dic1)

    def dictionaries_are_same1(self, dict_1, dict_2):
        unmatched_item = set(dict_1.items()) ^ set(dict_2.items())
        return len(unmatched_item) # should be 0


    def is_valid(self, list_of_maps):
        for map1 in list_of_maps:
            for map2 in list_of_maps:
                #if map1 == map2:
                if self.dictionaries_are_same1(map1, map2):
                    return False
                else:
                    return True

    def iterate_all2(self):
        for list in self.get_list_from_line():
            #print list
            list_of_maps = self.get_list_of_maps(list)
            #print list_of_maps
            if self.is_valid(list_of_maps):
                self.validPass += 1
            #print self.is_valid(list_of_maps)
            #adss


#p = Passphrase()
#p.iterate_all()
#print p.validPass

"""
pc = PassphraseContains()
pc.add('a')
pc.add('b')
pc.add('a')
print pc.map
"""

p = Passphrase()
p.iterate_all2()
print p.validPass
