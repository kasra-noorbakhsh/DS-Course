def mex_finder(array):
    items = set(array)
    for i in range(len(array)):
        if i not in items:
            return i
    return len(array)


list = []
number_of_numbers = int(input())

for i in range(number_of_numbers):
    sign, val = input().split()
    
    if(sign == '+'):
        list.append(int(val))

    elif(sign == '-'):
        if(int(val) in list):
            list.pop(list.index(int(val)))
    print(mex_finder(list))
