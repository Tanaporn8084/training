#print true ถ้าตัวเลขที่ผู้ใช้เดาทั้ง 2 ตัว อยู่ในลิสท์เลขนำโชค 
#print false ถ้ามีตัวเลขใดตัวเลขหนึ่งไม่อยู่ในลิสท์เลขนำโชค 
#หลังจากนั้น นำตัวเลข 2 ตัวแรกในเลขนำโชคออก
#แล้วเพิ่มตัวเลขที่ผู้ใช้กรอกทั้ง 2 ตัว ไปเป็นเลขนำโชคแทน 
#ทำได้ 2 วิธี วิธีที่ 1


lucky_number = [0,1,2,7]
n1 = int(input("เดาเลขที่1: "))
n2 = int(input("เดาเลขที่2: "))

print(n1 in lucky_number) and (n2 in lucky_number)

lucky_number.pop(0)
lucky_number.pop(0)

lucky_number.append(n1)
lucky_number.append(n2)

print(lucky_number)