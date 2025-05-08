def max_find(arr, n, k):
	
	trav, i = 0, 0
	c = 0
	maximum = 0

	while i < n - k + 1:
		trav = i - 1
		c = 0
		while trav >= 0 and arr[trav] == 0:
			trav -= 1
			c += 1
		trav = i + k
		
		while (trav < n and arr[trav] == 0):
			trav += 1
			c += 1
		c += k
		if (c > maximum):
			maximum = c
		i += 1

	return maximum

number_of_tests = int(input())
for i in range(number_of_tests) :
    length, k = [int(i) for i in input().split()]
    ser = list(input())
    ser = [eval(i) for i in ser]
    print(max_find(ser, length, k))
	