import math
import collections
from main import parse_vector


def main():
    # filename = 'input_test1.txt'
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

    collisions_data = collections.defaultdict(list)

    for idx0 in range(len(parcticles_list)-1):
        for idx1 in range(idx0+1, len(parcticles_list)):
            pos0, vel0, acc0 = parcticles_list[idx0]
            pos1, vel1, acc1 = parcticles_list[idx1]

            tx1, tx2 = solve_time(pos0[0], vel0[0], acc0[0], pos1[0], vel1[0], acc1[0])
            # print(tx1, tx2)
            ty1, ty2 = solve_time(pos0[1], vel0[1], acc0[1], pos1[1], vel1[1], acc1[1])
            # print(ty1, ty2)
            tz1, tz2 = solve_time(pos0[2], vel0[2], acc0[2], pos1[2], vel1[2], acc1[2])
            # print(tz1, tz2)
            # print()
            tx_list = [tx for tx in [tx1, tx2] if tx == None or tx > 0]
            ty_list = [ty for ty in [ty1, ty2] if ty == None or ty > 0]
            tz_list = [tz for tz in [tz1, tz2] if tz == None or tz > 0]
            if None in tx_list:
                tx_list.extend(ty_list)
                tx_list.extend(tz_list)
            if None in ty_list:
                ty_list.extend(tx_list)
                ty_list.extend(tz_list)
            if None in tz_list:
                tz_list.extend(tx_list)
                tz_list.extend(ty_list)

            # if tx1 >= 0 and tx2 >= 0:
            #     print(f'both tx are positive, tx1: {tx1}, tx2: {tx2}')
            # if ty1 >= 0 and ty2 >= 0:
            #     print(f'both ty are positive, ty1: {ty1}, tx2: {ty2}')
            # if tz1 >= 0 and tz2 >= 0:
            #     print(f'both tz are positive, tz1: {tz1}, tx2: {tz2}')
            matching_time = []
            for tx in tx_list:
                for ty in ty_list:
                    for tz in tz_list:
                        if tx == ty and ty == tz:
                            matching_time.append(tx)

            collistion_positions = []
            for t in matching_time:
                pos_t = []
                for i in range(3):
                    pos_t.append(position_at_t(pos0[i], vel0[i], acc0[i], t))
                collistion_positions.append(pos_t)

            for t, pos in zip(matching_time, collistion_positions):
                collisions_data[t].append((idx0, idx1, pos))
    # print(collisions_data)
    # exit()

    eliminated_idxs = []
    # collisions_data = sorted(collisions_data, key=lambda x: x[0])
    # last_colision_time = None
    # for t, idx0, idx1 in collisions_data:
    # print(list(sorted(collisions_data.keys())))
    # exit()
    for t in sorted(collisions_data.keys()):
        data_list = collisions_data[t]

        # eliminate non-existing particles from the data list
        non_existing = []
        for i, (idx0, idx1, _) in enumerate(data_list):
            if idx0 in eliminated_idxs or idx1 in eliminated_idxs:
                non_existing.append(i)
        non_existing = reversed(sorted(non_existing))
        for i in non_existing:
            data_list.pop(i)

        for idx0, idx1, _ in data_list:
            if idx0 not in eliminated_idxs:
                eliminated_idxs.append(idx0)
            if idx1 not in eliminated_idxs:
                eliminated_idxs.append(idx1)

        # if last_colision_time == t:
        #     if idx0 not in eliminated_idxs:
        #         eliminated_idxs.append(idx0)
        #     if idx1 not in eliminated_idxs:
        #         eliminated_idxs.append(idx1)
        # else:
        #     last_colision_time = t
        #     if idx0 in eliminated_idxs or idx1 in eliminated_idxs:
        #         continue
        #     else:
        #         eliminated_idxs.append(idx0)
        #         eliminated_idxs.append(idx1)

    # print(eliminated_idxs)
    print(len(eliminated_idxs))
    el = set(eliminated_idxs)
    print(len(el))

    print('answ = ', len(parcticles_list) - len(eliminated_idxs))

    # idx0 = 3
    # idx1 = 58
    # idx2 = 59
    # idx3 = 60

    # pos0, vel0, acc0 = parcticles_list[idx0]
    # pos1, vel1, acc1 = parcticles_list[idx1]
    # pos2, vel2, acc2 = parcticles_list[idx2]
    # pos3, vel3, acc3 = parcticles_list[idx3]

    # for i in range(3):
    #     print(solve_time(pos1[i], vel1[i], acc1[i], pos2[i], vel2[i], acc2[i]))

    # print()
    # pos_t = []
    # for i in range(3):
    #     pos_t.append(position_at_t(pos0[i], vel0[i], acc0[i], 2))
    # print(pos_t)

    # pos_t = []
    # for i in range(3):
    #     pos_t.append(position_at_t(pos1[i], vel1[i], acc1[i], 10))
    # print(pos_t)

    # pos_t = []
    # for i in range(3):
    #     pos_t.append(position_at_t(pos2[i], vel2[i], acc2[i], 10))
    # print(pos_t)

    # pos_t = []
    # for i in range(3):
    #     pos_t.append(position_at_t(pos3[i], vel3[i], acc3[i], 10))
    # print(pos_t)


def position_at_t(p0, v0, a, t):
    return p0 + t * v0 + 0.5 * (t**2 + t) * a


def solve_time(p01, v01, a1, p02, v02, a2):
    if a1 == 0 and a2 == 0:
        if v01 - v02 == 0 and p01 != p01:
            return -1, -1
        elif v01 - v02 == 0:
            return None, None
        t = (p02 - p01) / (v01 - v02)
        if round(t) != t:
            t = -1
        return -1, t
    if a1 - a2 == 0:
        return -1, -1
    delta = 0.25 * (2 * (v01 - v02) + (a1 - a2))**2 - 2 * (a1 - a2) * (p01 - p02)
    # print(delta)
    if delta < 0:
        return -1, -1
    t1 = (-(v01 - v02) - 0.5 * (a1 - a2) + math.sqrt(delta)) / (a1 - a2)
    t2 = (-(v01 - v02) - 0.5 * (a1 - a2) - math.sqrt(delta)) / (a1 - a2)
    # t1 = round(t1)
    # t2 = round(t2)
    if t1 != round(t1):
        t1 = -1
    if t2 != round(t2):
        t2 = -1
    return t1, t2


if __name__ == '__main__':
    main()
