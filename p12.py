# Source Link : https://edabit.com/challenge/WXqH9qvvGkmx4dMvp
# Level : Medium

def fizz_buzz(num):
  if num % 3 != 0 and num % 5 != 0:
    return str(num)

  result = ""

  if num % 3 == 0:
    result += "Fizz"
  
  if num % 5 == 0:
    result += "Buzz"

  return result