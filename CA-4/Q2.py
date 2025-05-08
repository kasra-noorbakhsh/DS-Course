graph = {}

def conect(graph):
    
    black_vertex = set()
    stack = [next(iter(graph))]

    while stack:
        vertex = stack.pop()
        if vertex not in black_vertex:
            black_vertex.add(vertex)
            stack.extend(child for child in graph[vertex] if child not in black_vertex)

    result = 0
    if(len(black_vertex) == len(graph)) :
        result = 1

    return result

number_of_vertexes, number_of_edges = map(int, input().split())

for i in range(number_of_vertexes):
    graph[i + 1] = []

for i in range(number_of_edges):
    u, v = map(int, input().split())
    graph[v].append(u)
    graph[u].append(v)

removed = set()

for j in range(number_of_vertexes):
    test_case = int(input())
    if conect(graph):
        print("YES")

    else:
        print("NO")

    removed.add(test_case)

    for neighbor in graph[test_case]:
        graph[neighbor].remove(test_case)
    graph.pop(test_case)