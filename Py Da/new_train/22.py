guest_a = ["josh","dadi","boy","man"]
name =input("what is your name?")
if name in guest_a:
    print("welcome")
else:
    print("you are not invited")

guest_a = ["josh","dadi","boy","man"]
name =input("what is your name?")
if name not in guest_a:
    print("you are not invited")
else:
    print("welcome")

name_o = "josh!snow"
name_n = name_o
name_o = "josh tillman"
print(name_o , name_n)


list_o=[1,2,3]
list_new = list_o
list_o[0] = -5
print("original:",list_o, "\nnew:",list_new)

list_o=[1,2,3]
list_new = list_o[:2]
list_o[0] = -5
print("original:",list_o, "\nnew:",list_new)