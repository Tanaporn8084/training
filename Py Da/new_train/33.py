grades = {
    "Alice": 85,
    "Bob": 90,               
}
print("original grades:",grades)
grades["Alice"] = 95
print("updated grades:",grades)

grades.update((("Alice", 95), ("Bob", 92)))
print("grades after update:", grades)

if "Alice" in grades:
    print("Alice's grade:", grades["Alice"])

#del grades["Alice"]
#print("grades after deleting Alice:", grades)

for el in grades.keys():
    print(el)

for el in grades:
    print(el)

for el in grades.values():
    print(el)

for person, grade in grades.items():
    print(person ,"has a grade of" ,grade)