# Source link : https://edabit.com/challenge/gt9LLufDCMHKMioh2
# Level : Easy

def stutter(text):
    if len(text) < 3:
        print("Text length should be at least 3")
        return

    word = text[0:2]
    print("{}... {}... {} ?".format(word , word , text[2:-1]))

input_text = input("Get your text ?")
stutter(input_text)