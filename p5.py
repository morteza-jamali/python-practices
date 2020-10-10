# Source link : https://edabit.com/challenge/FF6kYPHdAcJnoosr5
# Level : Easy

def factorial(num):
  result = 1
  num += 1
  for i in range(2 , num):
    result *= i
  
  return result

input_value = input("Get your number ?\n")
result = factorial(int(input_value))
print("This is factorial function result -> %s" % result)