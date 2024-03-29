from random import randint
from time import time
        

def partition(array, start, end):
    pivot = array[end]
    i = start - 1
    for j in range(start, end):
        if array[j] <= pivot:
            i += 1
            array[i], array[j] = array[j], array[i]
    array[i+1], array[end] = array[end], array[i+1]
    
    return i + 1

def quick_sort(array, start, end):
    if start < end:
        i = partition(array, start, end)
        
        quick_sort(array, start, i - 1)
        quick_sort(array, i+1, end)


def stats():
    run_times_small = []
    run_times_big = []
    for _ in range(5):
        numbers = [randint(0,100000000) for x in range(100)]
        start_time = time()
        quick_sort(numbers,0,len(numbers)-1)
        run_times_small.append(time()-start_time)

    for _ in range(5):
        numbers = [randint(0,100000000) for x in range(10000)]
        start_time = time()
        quick_sort(numbers,0,len(numbers)-1)
        run_times_big.append(time()-start_time)

    return run_times_small,run_times_big
