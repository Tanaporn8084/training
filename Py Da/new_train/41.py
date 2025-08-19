def get_day(user_info):
    day = int(input("what is your day of birth? "))
    user_info.append(day)

def get_month(user_info):
    month = int(input("what is your month of birth? "))
    user_info.append(month) 

def get_year(user_info):
    year = int(input("what is your year of birth? "))
    user_info.append(year)  

def get_user_bday(user_info):
    try:
        get_day(user_info)
        get_month(user_info)
        get_year(user_info)
        print("so your birthday is", user_info)
    except ValueError:
        print("Invalid input. Please enter a valid number for your birthday.")

print("Welcome to the birthday program")
user_info = []
get_user_bday(user_info)
#print("Thank you for using the birthday program")