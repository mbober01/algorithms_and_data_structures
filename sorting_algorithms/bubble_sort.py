from time import time
from random import randint

def bubble_sort(numbers):
    status = False
    start_time = time()
    n = len(numbers)
    for j in range(n):
        for i in range(1,n-j):
            if numbers[i] < numbers[i-1]:
                numbers[i],numbers[i-1] = numbers[i-1],numbers[i]
                status = True
                
        if not status:
            break
    run_time = time() - start_time
    return numbers, run_time

def stats():
    run_times_small = []
    run_times_big = []
    for _ in range(5):
        numbers = [randint(0,100000000) for x in range(100)]
        numbers, run_time = bubble_sort(numbers)
        run_times_small.append(run_time)
    
    for _ in range(5):
        numbers = [randint(0,100000000) for x in range(10000)]
        numbers, run_time = bubble_sort(numbers)
        run_times_big.append(run_time)

    return run_times_small,run_times_big
