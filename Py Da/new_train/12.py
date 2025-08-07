#answer_a = input("do you like travel? Y/N:")
#if answer_a =="Y":
    #answer_b = input("and do you like asia? Y/N:")
    #if answer_b == "Y":
        #print("excellent you can win a ticket")
    #else:
        #print("sorry to here that")
#else:
    #print("sorry to here that")


day = input("how many day ago have you purchased the item? ")
used = input("have you use the item at all? Y/N: ")
broke = input("has the item broken down on its own? Y/N: ")  

if (broke == "y" or (day <= 10 and used == "n")):
    print("you can get a refund")
else:
    print("you can not get a refund") 
    