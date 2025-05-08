q, p, x = [int(i) for i in input().split()]
number_we_can_buy = q // p
left = number_we_can_buy // x
remained = left + (number_we_can_buy % x)  
result = number_we_can_buy + left
while(remained >= x) :
    extra = remained // x
    result = result + extra
    remained = extra + (remained % x)
print(int(result))