

class Node(object):

    def __init__(self, _name, _weight, _children=[]):
        self.name = _name
        self.weight = _weight
        self.children_names = _children
        self.children = []

    def __str__(self):
        return "%s %d" % (self.name, self.weight)

    def add(self, node):
        if node.name in self.children_names:
            self.children.append(node)
        else:
            for ch in self.children:
                ch.add(node)


class Tree(object):

    def __init__(self):
        self.root = None

    def add(self, node):
        if self.root == None:
            self.root = node
        elif self.root.name in node.children_names:
            node.children.append(self.root)
            self.root = node
        else:
            self.root.add(node)

    def read_config(self):
        f = open("input.txt", 'r')
        table = []
        for elem in f:
            table.append(elem)
        return table

    def parse_string_to_Node(self, string):
        l = string.split()
        #print l
        name = l[0]
        w = int(l[1][1:len(l[1])-1])

        ch = []
        if len(l) > 2:
            ch = l[3:len(l)]

        #print ch
        return Node(name, w, ch)

    def parse_strings_to_nodes(self):
        table = []
        for s in self.read_config():
            n = self.parse_string_to_Node(s)
            #self.add(n)
            table.append(n)
        #for tab in table:
        #    print tab
        return table

    def build_Tree(self):
        table = self.parse_strings_to_nodes()
        self.leafs = []
        self.nodes = []

        for elem in table:
            if elem.children_names == []:
                self.leafs.append(elem)
            else:
                self.nodes.append(elem)

        for n in self.nodes:
            #print n
            self.add(n)



t = Tree()
t.read_config()
#print t.table[0]
#t.parse_strings_to_nodes()
t.build_Tree()
print t.root
