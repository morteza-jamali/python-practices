# Source Link : https://edabit.com/challenge/eADRy5SA5QbasA3Qt
# Level : Medium

def is_harshad(num):
  if num <= 9:
    return num

  number = num
  sum = 0

  while True:
    sum += num - ( num // 10 ) * 10
    num = num // 10

    if num <= 9:
      sum += num
      break

  return number % sum == 0