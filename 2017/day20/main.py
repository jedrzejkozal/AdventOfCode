import numpy as np


def main():
    # filename = 'input_test.txt'
    filename = 'input.txt'
    particles_spec = []
    with open(filename, 'r') as f:
        for line in f.readlines():
            particles_spec.append(line)

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

    for _ in range(1000):
        for i, (postion, velocity, accelaration) in enumerate(parcticles_list):
            # advance particle
            velocity += accelaration
            postion += velocity

            parcticles_list[i] = [postion, velocity, accelaration]

    distances = [np.sum(np.abs(pos)) for pos, _, _ in parcticles_list]
    i = np.argmin(distances)
    print(i)


def parse_vector(vector_str: str):
    vector_str = vector_str[3:].strip('>').strip('>\n')
    # print(vector_str)
    x, y, z = vector_str.split(',')
    x, y, z = int(x), int(y), int(z)
    vec = np.array([x, y, z])
    return vec


if __name__ == '__main__':
    main()
