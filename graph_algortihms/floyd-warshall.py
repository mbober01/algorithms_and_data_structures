def floyd_warshall(graph):
    size = len(graph[0])
    d = [[99999 if graph[j][i] == 0 and i != j else graph[j][i] for i in range(size)] for j in range(size)] # dlugosci pomiedzy krawedziami
    p = [[j+1 if graph[j][i] != 0 else 0 for i in range(size)] for j in range(size)] # poprzedniki 
    for u in range(size):
        for v in range(size):
            if d[v][u] != 0:
                for w in range(size):
                    if d[u][w] != 0:
                        l = d[v][u] + d[u][w]
                        if l < d[v][w]:
                            d[v][w] = l
                            p[v][w] = p[u][w]

    return [d, p]

def show_stats(stats):
    print("d")
    print("------------------------")
    for x in stats[0]:
        print(x)

    print("p")
    print("------------------------")
    for x in stats[1]:
        print(x)

def show_path(stats, start, d):
    print("--------------------------")
    print(f"shortest path from {start} to {d}")
    start = start - 1
    location = d - 1
    position = stats[1][start][location] - 1
    path = []
    while position != start:
        path.insert(0,[position + 1, location + 1])
        location = position
        position = stats[1][start][location] - 1
    path.insert(0,[position + 1, location + 1])
    for x in path:
        print(f"{x[0]} -> {x[1]}")
    print(f"distance = {stats[0][start][d-1]}")
    print("--------------------------")

graph = [[0,1,5,0,0,0,0],
         [0,0,2,0,0,0,0],
         [0,0,0,0,0,0,0],
         [7,0,0,0,1,0,0],
         [0,0,0,0,0,1,0],
         [2,0,0,4,0,0,0],
         [6,0,0,0,0,3,0]]



stats = floyd_warshall(graph)
show_stats(stats)
show_path(stats,5,3)