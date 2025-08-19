def unique_list(number_list):
    unique_numbers = []
    for number in number_list:
        if number not in unique_numbers:
            unique_numbers.append(number)
    return unique_numbers
print(unique_list([1, 2, 2, 3, 4, 4, 5]))   
print(unique_list([1, 1, 1, 1, 1]))
print(unique_list(["mark","mark","john","anna"]))

