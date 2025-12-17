

class Node(object):

    def __init__(self, _name, _weight, _children=[]):
        self.name = _name
        self.weight = _weight
        self.children_names = _children
        self.children = []

    def __str__(self):
        return "%s %d" % (self.name, self.weight)

    def __repr__(self):
        return f'Node({self.name})'

    def add(self, node) -> bool:
        # print()
        # print('adding node ', node)
        # print('current node = ', self.name)
        # print('current node children = ', self.children_names)
        # print(node.name in self.children_names)
        if node.name in self.children_names:
            self.children.append(node)
            return True
        else:
            adding_results = []
            for child in self.children:
                adding_results.append(child.add(node))
            return any(adding_results)


class Tree(object):

    def __init__(self):
        self.root = None

    def read_config(self, filename):
        f = open(filename, 'r')
        line_list = []
        for elem in f:
            line_list.append(elem)
        return line_list

    def parse_string_to_node(self, line):
        l = line.split()
        name = l[0]
        weight = int(l[1][1:len(l[1])-1])

        children_list = []
        if len(l) > 2:
            children_list = l[3:len(l)]
        children_list = [child_str[:-1] if child_str[-1] == ',' else child_str for child_str in children_list]

        return Node(name, weight, children_list)

    def parse_strings_to_nodes(self, line_list):
        node_list = []
        for line in line_list:
            node = self.parse_string_to_node(line)
            node_list.append(node)
        return node_list

    def build_tree(self, filename):
        line_list = self.read_config(filename)
        node_list = self.parse_strings_to_nodes(line_list)

        leafs = []
        nodes = []

        for elem in node_list:
            if elem.children_names == []:
                leafs.append(elem)
            else:
                nodes.append(elem)

        # for node in nodes:
        #     self.add(node)
        i = 0
        while len(nodes) > 0:
            node = nodes[i]
            if self.add(node):
                nodes.pop(i)
                if i >= len(nodes):
                    i = 0
            else:
                i += 1
                if i >= len(nodes):
                    i = 0

        for node in leafs:
            assert self.add(node)

    def add(self, node):
        if self.root == None:
            self.root = node
            return True
        elif self.root.name in node.children_names:
            node.children.append(self.root)
            self.root = node
            return True
        else:
            return self.root.add(node)


def main():
    tree = Tree()
    tree.build_tree("input.txt")
    # tree.build_tree("input_test.txt")
    # print(tree.root)

    # print(tree.root.children[2].children)

    whole_weight = get_weights(tree.root, {})
    print(whole_weight)


def get_weights(node: Node, cache: dict):
    children_weights = []
    for child in node.children:
        if child.name in cache:
            children_weights.append(cache[child.name])
        else:
            child_weight = get_weights(child, cache)
            cache[child.name] = child_weight
            children_weights.append(child_weight)

    if not all(weight == children_weights[0] for weight in children_weights):
        raise ValueError(f'imbalanced node found: {node.name} {children_weights} {[n.name for n in node.children]}')

    return sum(children_weights) + node.weight


if __name__ == '__main__':
    main()
