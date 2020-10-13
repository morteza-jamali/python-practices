# Source Link : https://edabit.com/challenge/pfn6QRn6eiTHEPpSs
# Level : Medium

def int_to_str(num):
    numbers_str = ['0' , '1' , '2' , '3' , '4' , '5' , '6' , '7' , '8' , '9']
    converted_number = ""
    number = num

    if num <= 9:
      return numbers_str[num]

    while True:
      if number <= 9:
        converted_number += numbers_str[number]
        break

      n = number - (number // 10) * 10
      converted_number += numbers_str[n]
      number = number // 10

    return converted_number[::-1]

def str_to_int(str):
  str_numbers = {"0":0 , "1":1 , "2":2 , "3":3 , "4":4 , "5":5 , "6":6 , "7":7 , "8":8 , "9":9}
  number = 0

  for i in str:
    number = number * 10 + str_numbers[i]

  return number