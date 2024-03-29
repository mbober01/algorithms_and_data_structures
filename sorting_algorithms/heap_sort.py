from random import randint
from time import time
def heapify(array, size, i):
    left = 2*i
    right = 2*i + 1
    
    max_i = i
    
    if left < size and array[i] < array[left]:
        max_i = left
    
    if right < size and array[max_i] < array[right]:
        max_i = right
    
    if i != max_i:
        array[max_i], array[i] = array[i], array[max_i]
        heapify(array, size, max_i)
        
def build_max_heap(array):
    size = len(array)
    for i in range(size//2, 0, -1):
        heapify(array,size,i)

def heap_sort(array):
    build_max_heap(array)
    for i in range(len(array)-1,1,-1):
        array[i], array[1] = array[1], array[i]
        heapify(array,i,1)
        
        
def stats():
    run_times_small = []
    run_times_big = []
    for _ in range(5):
        numbers = [randint(0,100000000) for x in range(100)]
        start_time = time()
        numbers.insert(0,None)
        heap_sort(numbers[1:])
        run_times_small.append(time()-start_time)
        
    for _ in range(5):
        numbers = [randint(0,100000000) for x in range(10000)]
        start_time = time()
        numbers.insert(0,None)
        heap_sort(numbers[1:])
        run_times_big.append(time()-start_time)
    
    return run_times_small,run_times_big