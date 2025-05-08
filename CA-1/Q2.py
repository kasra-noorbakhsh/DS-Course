temp = input().split()
number_of_people = int(temp[0])
quer_cnt = int(temp[1])
input_rocks = str(input())

quer = quer_cnt*[0]

for i in range(quer_cnt):
    quer[i] = int(input())

array = 10*[0]
ans = number_of_people*[0]

for i in range(number_of_people) :
    cur = int(ord(input_rocks[i]) - ord('0'))
    array[cur] += 1
    for j in range(10):
        ans[i] += abs(array[j] * (cur - j))
for i in quer:
    print(ans[i-1])