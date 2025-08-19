number = [1,2,3,4]
countries = ["uk","us","germany"]
countries =[1,"uk",2,"us"]
calls = [["a1","a2","a3"],["b1","b2","b3"]]
print(calls[0])

print(calls[0][0])

print(calls[0][1])

print(calls[1][2])

calls = [["a1","a2","a3"],["b1","b2","b3"]]
for x in calls:
    print("element:",x)

calls = [["a1","a2","a3"],["b1","b2","b3"]]
for x in calls:
    for y in x:
        print("element:",y)
table = [["a1","a2","a3"],["b1","b2","b3"]]
for row in table:
    for cell in row:
        print("element:",cell)