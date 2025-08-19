#and และ or ใช้เพื่อรวมเงื่อนไข boolean
#and จะได้ผลลัพธ์เป็น True เมื่อทั้งสองเงื่อนไขเป็น
#True ถ้าเงื่อนไขใดเงื่อนไขหนึ่งเป็น False จะได้ผลลัพธ์เป็น False
#or จะได้ผลลัพธ์เป็น True เมื่อเงื่อนไขใดเงื่อนไขหนึ่งเป็น True
#ถ้าเงื่อนไขทั้งสองเป็น False จะได้ผลลัพธ์เป็น False  

#ตัวอย่างการใช้ and
x = 5
y = 10
if x < y and y > 5:
    print("Both conditions are True")  #จะพิมพ์ข้อความนี้เพราะ x น้อยกว่า y และ y มากกว่า 5
#ตัวอย่างการใช้ or
if x < y or y < 5:
    print("At least one condition is True")  #จะพิมพ์ข้อความนี้เพราะ x น้อยกว่า y
#ตัวอย่างการใช้ and และ or ร่วมกัน
if (x < y and y > 5) or (x == 5):
    print("Complex condition is True")  #จะพิมพ์ข้อความนี้เพราะ x น้อยกว่า y และ y มากกว่า 5    
#ตัวอย่างการใช้ and และ or กับ boolean
x = True    
y = False

print(x and y)  #จะได้ผลลัพธ์เป็น False เพราะ y เป็น False
print(x or y)   #จะได้ผลลัพธ์เป็น True เพราะ x เป็น True 


x = 5==3
y = "H" in "Hello"

print(x and y)
print(x or y)