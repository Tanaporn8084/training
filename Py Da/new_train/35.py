#print("hello","how are you", end=".",sep="-")

def print_letter_count(text, letter="t"):
    count = 0
    for char in text:
        if char == letter:
            count += 1
    print("The letter", letter, "appears", count, "times in the text.")
print_letter_count("how many letters are in this text?",)