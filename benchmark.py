import time

def benchmark():
    start = time.time()
    data = sorted([i for i in range(100000, 0, -1)])
    end = time.time()
    return end - start

if __name__ == "__main__":
    runs = 5
    times = [benchmark() for _ in range(runs)]
    average_time = sum(times) / runs
    print("Execution times: {}".format(times))
    print("Average execution time: {}".format(average_time))
