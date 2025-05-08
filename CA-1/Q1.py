number_of_people, percent = [int(i) for i in input().split()]
names_of_people = input().split(',')
points_of_people = [int(i) for i in input().split(',')]
number_of_up_percents = number_of_people * percent / 100
tuple_of_people_and_points = list(zip(names_of_people, points_of_people))
tuple_of_people_and_points.sort(key = lambda x : x[1] , reverse = True)
names = list(zip(*tuple_of_people_and_points))[0]
res = list(names[:int(number_of_up_percents)])
the_rest = list(names[int(number_of_up_percents):])
the_rest.sort()
res += the_rest
for i in range(len(res)) :
    print(res[i] , end = ' ')