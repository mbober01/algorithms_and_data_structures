from time import time
from random import randint

def merge_sort(array):
    if len(array) > 1:
        left_array = array[:len(array)//2]
        right_array = array[len(array)//2:]
        merge_sort(left_array)
        merge_sort(right_array)
        i = 0
        j = 0
        arr_index = 0
        while i < len(left_array) and j < len(right_array):
            if left_array[i] < right_array[j]:
                array[arr_index] = left_array[i]
                i += 1
            else:
                array[arr_index] = right_array[j]
                j += 1
            arr_index += 1
            
        while i < len(left_array):
            array[arr_index] = left_array[i]
            i += 1
            arr_index += 1
            
        while j < len(right_array):
            array[arr_index] = right_array[j]
            j += 1
            arr_index += 1
            
            
def stats():        
    run_times_small = []
    run_times_big = []
    for _ in range(5):
        numbers = [randint(0,100000000) for x in range(100)]
        start_time = time()
        merge_sort(numbers)
        run_times_small.append(time()-start_time)

    for _ in range(5):
        numbers = [randint(0,100000000) for x in range(10000)]
        start_time = time()
        merge_sort(numbers)
        run_times_big.append(time()-start_time)
        
    return run_times_small,run_times_big
