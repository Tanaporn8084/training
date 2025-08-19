def get_average(input_numbers):
    total = 0.0
    for number in input_numbers:
        total += number
    average = total / len(input_numbers)
    return average
print("the average is:",get_average([5.0, 10.0, 15.0, 20.0, 25.0]))

average = get_average([5.0, 10.0, 15.0, 20.0, 25.0])
if average > 10:
    print("The average is greater than 10.")    

def is_first_last_equal(number_list):
    if number_list[0] == number_list[-1]:
        return True
    else:
        return False
print(is_first_last_equal([1, 2, 3, 4, 1]))

print(is_first_last_equal([1, 2, 3, 4, 5]))




    

