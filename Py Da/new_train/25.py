table = [["a1","a2","a3"],["b1","b2","b3"]]
for row in table:
    for cell in row:
        print(cell, " , end")
    print()

table =[[i for i in range(1,6)] for j in range(4)]
print(table)