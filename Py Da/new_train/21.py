#first = input("enter first number: ")
#second = input("enter second number: ")
#print("before swapping:",first, second)
#first , second = second , first
#first = second
#second = first 
#print("after swapping:",first, second)

top_city = ["new york","bangkok","hanoi","mexico"]
top_city[0] , top_city[3] = top_city[3] , top_city[0]
print(top_city) 

top_city = ["new york","bangkok","hanoi","mexico"]
top_city[1] , top_city[0] = top_city[0] , top_city[1]
print(top_city) 

top_city = ["new york","bangkok","hanoi","mexico"]
top_city.sort()
print(top_city)
 
#เรียงจากน้อยไปมาก
random = [2,5,0,-3,4]
random.sort()
print(random)

#เรียงจากมากไปน้อย
random = [2,5,0,-3,4]
random.sort(reverse=True)
print(random)

top_city = ["new york","bangkok","hanoi","mexico"]
print(sorted(top_city))
print(top_city) 