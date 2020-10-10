# Source link : https://edabit.com/challenge/8pDH2SRutPoaQghgc
# Level : Easy

relations = {
    "Darth Vader" : "father" ,
    "Leia" : "sister" ,
    "Han" : "brother in law" ,
    "R2D2" : "droid"
}

def relation_to_luke(name):
    if name in relations:
        return "Luke, I am your %s." % relations[name]
    else:
        return "I don't khow who you are !"

input_value = input("Get your name ?\n")
result = relation_to_luke(input_value)
print(result)