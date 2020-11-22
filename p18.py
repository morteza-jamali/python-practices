# Source Link : https://edabit.com/challenge/2zKetgAJp4WRFXiDT
# Level : Medium

def number_length(num):
  length = 0

  while True:
    num = num // 10
    length += 1

    if num == 0:
      break

  return length