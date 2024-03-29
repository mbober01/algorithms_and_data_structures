from random import randint
from time import time
def insert_sort(numbers):
    start_time = time()
    for i in range(1, len(numbers)):
        temp = numbers[i]
        j = i - 1
        while temp < numbers[j] and j >= 0:
            numbers[j+1] = numbers[j]
            j -= 1
        numbers[j+1] = temp
    run_time = time() - start_time
    return numbers, run_time


def stats():
    run_times_small = []
    run_times_big = []
    for _ in range(5):
        numbers = [randint(0,100000000) for x in range(100)]
        numbers, run_time = insert_sort(numbers)
        run_times_small.append(run_time)

    for _ in range(5):
        numbers = [randint(0,100000000) for x in range(10000)]
        numbers, run_time = insert_sort(numbers)
        run_times_big.append(run_time)
        
    return run_times_small,run_times_big