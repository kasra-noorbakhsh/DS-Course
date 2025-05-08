from collections import deque

def maxfinder(arr, K):
    res = []
    Q = deque()
    for i in range(K):
        while Q and arr[i] >= arr[Q[len(Q) - 1]]:
            Q.pop()
        Q.append(i)

    for i in range(K, len(arr)):
        res.append(arr[Q[0]])
        while Q and Q[0] <= i-K:
            Q.popleft()
        while Q and arr[i] >= arr[Q[len(Q) - 1]]:
            Q.pop()
        Q.append(i)
    res.append(arr[Q[0]])
    
    return res



n, k = [int(i) for i in input().split()]
input_arr = [int(i) for i in input().split()]
q = input()

result = maxfinder(input_arr, k)

indexes = []

for j in range(int(q)) :
    indexes.append(int(input()))

for a in range(int(q)) :
    print(result[indexes[a] - k])