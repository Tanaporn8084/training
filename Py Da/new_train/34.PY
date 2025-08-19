def get_average(input_numbers):
    sum = 0.0
    for number in input_numbers:
        sum += number
    average = sum / len(input_numbers)
    print(average)

get_average ([5.0, 10.0, 15.0, 20.0, 25.0])

#การนับจำนวนตัวอักษรในข้อความ
def prin_letter_count(tex,letter):
    count = 0
    for char in tex:
        if char == letter:
            count += 1
    print("The letter", letter, "appears", count, "times in the text.")
prin_letter_count("hello world", "p")