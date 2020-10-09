def is_curzon(number):
    num1 = 2 ** float(number) + 1
    num2 = 2 * float(number) + 1
    return (num1 % num2) == 0

input_value = input("Get your number ?\t")

if is_curzon(input_value):
    print("Your number is curzon")
else:
    print("Your number isn't curzon")