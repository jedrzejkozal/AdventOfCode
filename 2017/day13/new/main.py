from copy import deepcopy


class Firewall:

    def __init__(self, config: dict):
        self.n_layers = max(config.keys()) + 1
        self.firewall_layers = deepcopy(config)
        self.scanner_positions = {key: 0 for key in config}
        self.reverse_direction = {key: False for key in config}

    def advance_scaners(self):
        for layer_idx, scaner_pos in self.scanner_positions.items():
            layer_range = self.firewall_layers[layer_idx]
            if scaner_pos == layer_range - 1:
                self.reverse_direction[layer_idx] = True
            elif scaner_pos == 0:
                self.reverse_direction[layer_idx] = False

            if self.reverse_direction[layer_idx]:
                self.scanner_positions[layer_idx] -= 1
            else:
                self.scanner_positions[layer_idx] += 1

    def __repr__(self):
        firewall_str = ''
        for key, layer_range in self.firewall_layers.items():
            layer_str = ''
            for cell_idx in range(layer_range):
                cell_str = '[ ]'
                if cell_idx == self.scanner_positions[key]:
                    cell_str = '[S]'
                layer_str += cell_str
            firewall_str += f'{key}: {layer_str}\n'
        return firewall_str


def main():
    # config = {0: 3, 1: 2, 4: 4, 6: 4}
    config = load_config()

    firewall = Firewall(config)
    for _ in range(9):
        firewall.advance_scaners()

    # print(simulate_pass(deepcopy(firewall)))

    caught = True
    delay_run = 10
    while caught:
        firewall.advance_scaners()
        caught = simulate_pass(deepcopy(firewall))
        if not caught:
            break
        delay_run += 1
        if delay_run % 1000 == 0:
            print(delay_run)
    print(delay_run)


def simulate_pass(firewall):
    was_caught = False
    # penalty = 0
    packet_pos = -1
    for layer_idx in range(firewall.n_layers):
        packet_pos += 1
        if packet_pos in firewall.scanner_positions and firewall.scanner_positions[packet_pos] == 0:  # caught
            # penalty += layer_idx * firewall.firewall_layers[layer_idx]
            was_caught = True
        firewall.advance_scaners()
        # print(firewall)
        # exit()

    # print(penalty)
    return was_caught


def load_config():
    config = {}
    with open('input.txt', 'r') as f:
        for line in f.readlines():
            key, value = line.split(':')
            key, value = int(key), int(value)
            config[key] = value
    return config


if __name__ == '__main__':
    main()
