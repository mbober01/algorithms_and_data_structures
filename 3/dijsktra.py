def find_min(tab):
    minimum = max(tab)
    for x in tab:
        if x < minimum and x != 0:
            minimum = x

    return minimum

# def row(graph, vertex):
#     return graph[vertex][:vertex] + graph[vertex][vertex+1:]

#algorytm dijkstry dla grafu zaczynajac od punktu start
def dijkstra_algorithm(graph, start):
    start = start - 1
    length = len(graph)
    nums = [[x+1 for x in range(length)], # kolejka priorytetowa na index 0 wszystkie punkty grafu na index 1 ich dist
            [99999 for x in range(length)]]
    stats = [[x+1 for x in range(length)], # statystyki do wypisania na koniec algorytmu 
            [None for x in range(length)],
            [99999 for x in range(length)]]
    
    vertex = nums[0][start] - 1 
    stats[1][vertex] = 0 
    stats[2][vertex] = 0
    while nums[0]: 
        i = 0
        for x in graph[vertex]:
            d = x + stats[2][vertex] # d to dlugosc aktualnego badanego elementu i dlugosc do elementu z grafu
            if stats[2][i] > d and x != 0 and i+1 in nums[0]: # spisanie nowych danych jeżeli długość jest mniejsza
                stats[1][i] = vertex+1 
                stats[2][i] = d
                ind = nums[0].index(i+1) # aktualizacja kolejki priorytetowej
                nums[1][ind] = d  
            i += 1

        min_connection = find_min(nums[1]) # znalezienie kolejnego elemntu
        ind = nums[1].index(min_connection)
        vertex = nums[0][ind] - 1
        nums[0].pop(ind)  
        nums[1].pop(ind)
    return stats

# najkrotsza trasa dla grafu od start do end
def shortest_path(graph, start, end):
    print("---------------------------")
    print(f"shortest path from {start} to {end}")
    stats = dijkstra_algorithm(graph, start) 
    location = end 
    path = [] 
    while location != start:
        path.insert(0, [stats[1][location-1], location]) # na 0 indexie skad na 1 indexie dokad
        location = stats[1][location-1] # zmiana location na pred ze stats
    for x in path:
        print(f"{x[0]} -> {x[1]}")
    print(f"distance = {stats[2][end-1]}")
    print("---------------------------")
    

graph = [[0,3,0,3,5],
         [3,0,5,1,0],
         [0,5,0,2,0],
         [3,1,2,0,1],
         [5,0,0,1,0]]


algorithm = dijkstra_algorithm(graph, 1) 
shortest_path(graph, 1, 3) 


print("---------------------------")
print(f"v    | {algorithm[0]}")
print(f"pred | {algorithm[1]}")
print(f"dist | {algorithm[2]}")
print("---------------------------")