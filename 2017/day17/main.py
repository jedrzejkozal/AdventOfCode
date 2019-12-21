import time
import matplotlib.pyplot as plt

def spinlock(step=3, num_steps=2017):
    buffer = [0]
    current_position = 0
    for i in range(1, num_steps+1):
        current_position = (current_position + step) % i
        current_position += 1
        buffer.insert(current_position, i)
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

def get_result(buffer, index):
    index = buffer.index(2017)
    index = (index+1) % len(buffer)
    return buffer[index]

if __name__ == '__main__':
    steps = [100, 1000, 10000] #, 100000]
    t = []
    for s in steps:
        duration = measure_time_for_n_steps(s)
        t.append(duration)
        print("steps = {}, time = {}".format(s, duration))

    plot_time(steps, t)

    buffer = spinlock(step=359, num_steps=2017)
    print("value after 2017 = ", get_result(buffer, 2017))