from collections import deque

input_string = input()
stack = deque()
count = 0
result = 0
for i in range(len(input_string)) :
    if(input_string[i] == '(' or input_string[i] == '{' or input_string[i] == '[') :
        stack.append(input_string[i])
        count += 1
    elif(input_string[i] == ')' and len(stack) != 0) :
        if(stack[-1] == '(') :
            stack.pop()
            count += 1
        else :
            stack = deque()
            count = 0
    elif(input_string[i] == '}' and len(stack) != 0) :
        if(stack[-1] == '{') :
            stack.pop()
            count += 1
        else :
            stack = deque()
            count = 0
    elif(input_string[i] == ']' and len(stack) != 0) :
        if(stack[-1] == '[') :
            stack.pop()
            count += 1
        else :
            stack = deque()
            count = 0
    if(len(stack) == 0 and i > 0) :
        if(count > result) :
            result = count
print(result)