def find_min(tab):
    minimum = max(tab)
    for x in tab:
        if x < minimum and x != 0:
            minimum = x

    return minimum

def row(graph, vertex):
    return graph[vertex][:vertex] + graph[vertex][vertex+1:]

def dijkstra_algorithm(graph):
    length = len(graph)
    nums = [[x+1 for x in range(length)],
            [99999 for x in range(length)]]
    stats = [[x+1 for x in range(length)],
            [None for x in range(length)],
            [99999 for x in range(length)]]
    
    vertex = nums[0][0] - 1
    stats[1][vertex] = 0
    stats[2][vertex] = 0
    while nums[0]:
        i = 0
        for x in graph[vertex]:
            d = x + stats[2][vertex]
            if stats[2][i] > d and x != 0 and i+1 in nums[0]:
                stats[1][i] = vertex+1
                stats[2][i] = d
                try: # tu moze byc blad jakby co !!!!!!!!!!!!!!!!!!!
                    ind = nums[0].index(i+1)
                    nums[1][ind] = d
                except ValueError:
                    pass
            i += 1
        min_connection = find_min(nums[1])
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

mst = dijkstra_algorithm(graph)
print("---------------------------")
print(f"v    | {mst[0]}")
print(f"pred | {mst[1]}")
print(f"k    | {mst[2]}")
print("---------------------------")