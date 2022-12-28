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
            
numbers = [randint(-1000000,10000000) for _ in range(1000000)]
start_time = time()
merge_sort(numbers)
print(time() - start_time)
