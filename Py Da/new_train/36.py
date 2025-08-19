def show_truth():
    global mysterious_var 
    mysterious_var = "new surprise"
    print(mysterious_var)

mysterious_var = "surprise"
print(mysterious_var)
show_truth()
print(mysterious_var)

def show_truth():
    mysterious_var.append ("new surprise")
    print(mysterious_var)
mysterious_var = ["surprise"]
print(mysterious_var)
show_truth()
print(mysterious_var)