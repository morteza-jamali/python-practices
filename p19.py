# Source List : https://edabit.com/challenge/Hs7YDjZALCEPRPD6Z
# Level : Medium

def count_uppercase(arr):
  count = 0

  for v in arr:
    for w in v:
      if w.isupper():
        count += 1
  
  return count