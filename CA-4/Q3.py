graph = {}

number_of_test_cases = int(input())

def cal():
    for nodes in graph:
        for j in range(len(graph[nodes])):

            if(len(graph[graph[nodes][j]]) >= 2):
                if(nodes in graph[graph[nodes][j]]):
                    graph[graph[nodes][j]].pop(graph[graph[nodes][j]].index(nodes))
                    break

            if(j != len(graph[nodes]) - 1):
                continue
            print("NO")
            return
    print("YES")
    return

for _ in range(number_of_test_cases):
    sherkat_konande_ha, tedad_bazi_ha = map(int, input().split())
    for k in range(sherkat_konande_ha):
        graph[k + 1] = []

    for _ in range(tedad_bazi_ha):
        v,u = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)
    cal()