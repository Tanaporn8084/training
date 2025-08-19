def get_number():
    for i in range(1, 4):
        yield i
print((get_number()))

generator = get_number()
print(next(generator))      
print(next(generator))
print(next(generator))
 
for i in get_number():
    print(i)

number=list(get_number())
print(number)