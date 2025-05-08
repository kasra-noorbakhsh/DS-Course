import heapq

number_of_numbers , q = map(int, input().split())
numbers = [int(i) for i in input().split()]
numbers.sort() #

upper_bond = numbers[int(number_of_numbers / 2) :]
lower_bond = numbers[0:int(number_of_numbers / 2)]

max_heap = []
min_heap = upper_bond
for element in lower_bond:
    heapq.heappush(max_heap, -element) #because we neaded a max heap we did this

heapq.heapify(min_heap)

if(len(max_heap) > len(min_heap)):
    miane = -max_heap[0]
else:
    miane = min_heap[0]

for j in range(q):
    temp = input()

    if(int(temp) > miane):
        heapq.heappush(min_heap, int(temp))
    elif(int(temp) <= miane):
        heapq.heappush(max_heap, -int(temp))

    if(len(min_heap) - len(max_heap) > 1):
        temp_ = heapq.heappop(min_heap)
        heapq.heappush(max_heap, -temp_)
    elif(len(max_heap) - len(min_heap) > 1):
        _temp = -heapq.heappop(max_heap)
        heapq.heappush(min_heap, _temp)
    
    if(len(min_heap) > len(max_heap)):
        miane = min_heap[0]
    else:
        miane = -max_heap[0]
    print(miane)