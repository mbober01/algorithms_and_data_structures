from time import time
from random import randint

def bubble_sort(numbers):
    status = True
    start_time = time()
    n = len(numbers)
    for j in range(n):
        for i in range(1,n-j-1):
            if numbers[i] < numbers[i-1]:
                numbers[i],numbers[i-1] = numbers[i-1],numbers[i]
                status = True
                
        if not status:
            break
    run_time = time() - start_time
    return numbers, run_time


numbers = [randint(-1000000,10000000) for _ in range(1000000)]
numbers, run_time = bubble_sort(numbers)
print(run_time)