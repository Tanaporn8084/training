top_city = ["new york","bangkok","hanoi","tax"]
for city in top_city:
    print("current",city)

top_city = ["new york","bangkok","hanoi","tax"]
for city_index in range(len(top_city)):
    print("current index:",city_index, " current city:" , top_city[city_index])

spendings = [32.45,18.56,45.68,23.67]
sum = 0.0
for spend in spendings:
    sum += spend
print("money spent:",sum)



