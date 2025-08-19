#ใช้เพื่อดึงค่า value ทั้งหมดใน dictionary
#ใช้กับ dict ได้เท่านั้น  

my_dict = {"name":"Henry","age":21,"gender":"male"}

print(my_dict.values())
print(type(my_dict.values()))

#เปลี่ยนจาก dict_values เป็น list
print(type(list(my_dict.values())))