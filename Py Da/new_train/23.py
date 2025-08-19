number = [1,2,3,4]
number =[]
for i in range(1,101):
    number.append(i)
print(number)

numbers = [i for i in range(1,101)]
print(numbers)

numbers = [i for i in range(1,101)if i % 3 !=0]
print(numbers)