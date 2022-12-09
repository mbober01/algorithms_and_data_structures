from random import randint

def find_min(tab):
    minimum = max(tab)
    for x in tab:
        if x < minimum and x != 0:
            minimum = x

    return minimum


# algorytm prima dla grafu zaczynajac od losowego punktu 
def algorytm_prima(graph):
    length = len(graph)
    start = randint(1, length) 
    nums = [[x+1 for x in range(length)], # kolejka priorytetowa na index 0 wszystkie punkty grafu na index 1 ich k
            [99999 for x in range(length)]]
    stats = [[x+1 for x in range(length)], # statystyki do wypisania na koniec algorytmu 
            [None for x in range(length)],
            [99999 for x in range(length)]]
    vertex = nums[0][start-1]-1 
    stats[1][vertex] = 0 
    stats[2][vertex] = 0
    while nums[0]: 
        i = 0
        for x in graph[vertex]:
            if stats[2][i] > x and x != 0 and i+1 in nums[0]: # spisanie nowych danych jeżeli dlugosc jest mniejsza
                stats[1][i] = vertex+1 
                stats[2][i] = x
                ind = nums[0].index(i+1) # aktualizacja kolejki priorytetowej
                nums[1][ind] = x
            i += 1

        min_connection = find_min(nums[1]) # znalezienie kolejnego elementu 
        ind = nums[1].index(min_connection)
        vertex = nums[0][ind] - 1
        nums[0].pop(ind)
        nums[1].pop(ind)
    return stats




graph = [[0,3,0,3,5],
         [3,0,5,1,0],
         [0,5,0,2,0],
         [3,1,2,0,1],
         [5,0,0,1,0]]


mst = algorytm_prima(graph)
print("---------------------------")
print(f"v    | {mst[0]}")
print(f"pred | {mst[1]}")
print(f"k    | {mst[2]}")
print("---------------------------")
