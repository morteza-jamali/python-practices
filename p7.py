# Source List : https://edabit.com/challenge/QFXMcwaQZ8FTAuEtg
# Level : Easy

def counterpartCharCode(c):
    if c.isalpha():
        if c.islower():
            return ord(c.upper())
        elif c.isupper():
            return ord(c.lower())
    else:
        return ord(c)

input_value = input("Enter your character ?\n")
print(counterpartCharCode(input_value))