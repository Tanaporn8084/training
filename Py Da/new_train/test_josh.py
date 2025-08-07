oct1 = int(input('What is the 1st octet '))
oct2 = int(input('What is the 2nd octet '))
oct3 = int(input('What is the 3rd octet '))
oct4 = int(input('What is the 4th octet '))

if (oct4 ==0):
    print('This is a network address, Please renter')
    oct4 = int(input('Enter the 4th octet again '))
    
if (oct1==192):
    submaskC = ('255.255.255.0')
    print('Subnet mask is ', submaskC)
    
if (oct1==172):
    submaskB = ('255.255.0.0')
    print('Subnet mask is ', submaskB)

if (oct1==10):
    submaskA =('255.0.0.0')
    print('Your subnet mask is', submaskA)

print('Your ip address is')
print (oct1, oct2, oct3,oct4, sep='.')