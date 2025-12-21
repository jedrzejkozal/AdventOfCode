import numpy as np
import collections


def main():
    # filename = 'input_test1.txt'
    filename = 'input.txt'
    particles_spec = []
    with open(filename, 'r') as f:
        for line in f.readlines():
            particles_spec.append(line)

    for n in [1000]:
        n_left = simulation(particles_spec, n)
        print(f'{n}: particles left: {n_left}')


def simulation(particles_spec, n=100000):
    parcticles_list = []

    for spec in particles_spec:
        postion, velocity, accelaration = spec.split(', ')
        postion = parse_vector(postion)
        velocity = parse_vector(velocity)
        accelaration = parse_vector(accelaration)

        parcticles_list.append([postion, velocity, accelaration])

    # for p in parcticles_list:
    #     print(p)
    # print()

    for t_idx in range(n):
        pos_index = collections.defaultdict(list)
        for i, (postion, velocity, accelaration) in enumerate(parcticles_list):
            # advance particle
            velocity += accelaration
            postion += velocity

            parcticles_list[i] = [postion, velocity, accelaration]
            pos_hash = tuple(postion.tolist())
            pos_index[pos_hash].append(i)

        # Collect all particles that need to be removed
        particles_to_remove = set()
        for pos_list in pos_index.values():
            if len(pos_list) > 1:
                particles_to_remove.update(pos_list)

        # Remove particles in reverse order of index to avoid shifting issues
        for j in sorted(particles_to_remove, reverse=True):
            parcticles_list.pop(j)

        # for p in parcticles_list:
        #     print(p)
        # print()

    # distances = [np.sum(np.abs(pos)) for pos, _, _ in parcticles_list]
    # i = np.argmin(distances)
    # print(i)
    # print(len(parcticles_list))
    return len(parcticles_list)


def parse_vector(vector_str: str):
    vector_str = vector_str[3:].strip('>').strip('>\n')
    # print(vector_str)
    x, y, z = vector_str.split(',')
    x, y, z = int(x), int(y), int(z)
    vec = np.array([x, y, z])
    return vec


if __name__ == '__main__':
    main()
