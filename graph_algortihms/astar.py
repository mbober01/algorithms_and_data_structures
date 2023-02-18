def find_min(open0, open1, closed):
    minimum = 999999
    for x in open1:
        ind = open1.index(x)
        if x < minimum and x != 0 and open0[ind] not in closed:
            minimum = x

    return minimum

def a_algorithm(graph, start, d):
    start = start
    length = len(graph)
    open = [[],
            []] # otwarte v
    closed = [start] # zamkniete
    stats = [[x+1 for x in range(length)], # v
            [4,8,3,4,5,2,1,0], #przewidywania 
            [99999 for x in range(length)], # dlugosc z s do v
            [99999 for x in range(length)], # przewidywaa droga z s do d
            [0 for x in range(length)], # poprzedni v
            ]
    
    vertex = start - 1
    stats[2][vertex] = 0 
    stats[3][vertex] = stats[1][vertex]
    stats[4][vertex] = 0
    gv = 0
    while d not in closed:
        i = 0
        for x in graph[vertex]:
            if stats[2][i] != 99999:
                f = stats[2][i] + stats[1][i]
            else:
                f = x + stats[1][i] + gv
            if x != 0 and stats[3][i] > f and i + 1 not in closed:
                open[0].append(i+1)
                open[1].append(f)
                stats[2][i] = gv + x
                stats[3][i] = f
                stats[4][i] = vertex + 1

            i += 1
        minf = find_min(open[0], open[1], closed)
        ind = open[1].index(minf)
        vertex = open[0][ind] - 1
        open[0].pop(ind)
        open[1].pop(ind)
        closed.append(vertex+1)
        gv = stats[2][vertex]

    return stats

def show_path(graph, start, d):
    print("--------------------------")
    print(f"shortest path from {start} to {d}")
    stats = a_algorithm(graph,start,d)
    location = d
    path = []
    while location != start:
        path.insert(0, [stats[4][location-1], location])
        location = stats[4][location-1]
    for x in path:
        print(f"{x[0]} -> {x[1]}")
    print(f"distance = {stats[3][d-1]}")
    print("--------------------------")

def show_stats(stats):
    stats[2] = [0 if x == 99999 else x for x in stats[2]]
    stats[3] = [0 if x == 99999 else x for x in stats[3]]
    print("---------------------------")
    print(f"v    | {stats[0]}")
    print(f"h(v) | {stats[1]}")
    print(f"g(v) | {stats[2]}")
    print(f"f(v) | {stats[3]}")
    print(f"p    | {stats[4]}")
    print("---------------------------")

graph = [[0,5,0,1,0,0,0,0],
         [0,0,2,0,1,0,0,0],
         [0,0,0,0,0,0,0,3],
         [0,0,0,0,1,2,0,0],
         [0,0,4,0,0,0,0,0],
         [4,0,0,0,0,0,2,0],
         [0,0,0,0,1,0,0,1],
         [0,0,0,0,2,0,0,0]]


algorithm = a_algorithm(graph,1,8)
show_stats(algorithm)
show_path(graph, 1, 8)