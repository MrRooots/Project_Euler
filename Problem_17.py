# Count of chars in numbers
# num2words ----> 115 == one hundred and fifteen
def char_counting(count):
    from num2words import num2words
    result = 0
    for number in range(1, count + 1):
        for char in num2words(number):
            if char.isalpha() == True:
                result += 1
    return result

print(char_counting(int(input("Count: "))))