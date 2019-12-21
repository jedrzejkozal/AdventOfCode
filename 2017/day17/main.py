import time
import matplotlib.pyplot as plt


class LockNode:

    def __init__(self, v):
        self.value = v
        self.next_node = None

    def insert(self, new_node):
        new_node.next_node = self.next_node
        self.next_node = new_node


def spinlock(step=3, num_steps=2017):
    _, spinlock_root = compute_spinlock(step, num_steps)
    return spinlock2buffer(spinlock_root, num_steps)


def compute_spinlock(step, num_steps):
    spinlock_root = LockNode(0)
    spinlock_root.next_node = spinlock_root
    spinlock = spinlock_root

    for i in range(1, num_steps+1):
        for _ in range(step):
            spinlock = spinlock.next_node
        spinlock.insert(LockNode(i))
        spinlock = spinlock.next_node
    return spinlock, spinlock_root


def spinlock2buffer(spinlock_root, num_steps):
    buffer = []
    spinlock = spinlock_root
    while len(buffer) != num_steps+1:
        buffer.append(spinlock.value)
        spinlock = spinlock.next_node
    return buffer


def measure_time_for_n_steps(n):
    duration = 0.0
    for _ in range(1000):
        t0 = time.time()
        buffer = spinlock(step=359, num_steps=n)
        duration += time.time() - t0
    return duration / 1000


def plot_time(steps, t):
    plt.plot(steps, t)
    plt.xscale('log')
    plt.grid(True)
    plt.show()


def perform_time_analysis():
    steps = [100, 1000, 10000]  # , 100000]
    t = []
    for s in steps:
        duration = measure_time_for_n_steps(s)
        t.append(duration)
        print("steps = {}, time = {}".format(s, duration))

    plot_time(steps, t)


def main():
    spinlock, _ = compute_spinlock(step=359, num_steps=2017)
    solution1 = spinlock.next_node.value
    print("part 1 solution = ", solution1)

    _, spinlock_root = compute_spinlock(step=359, num_steps=50000000)
    solution2 = spinlock_root.next_node.value
    print("part 2 solution = ", solution2)

    # perform_time_analysis()


if __name__ == '__main__':
    main()
