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

numbers = [randint(1,100) for x in range(100000)]
numbers, run_time = insert_sort(numbers)
print(run_time)