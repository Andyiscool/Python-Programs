name = input("what's your name?")
print("Hello", name)
age = input("How old are you?")
print(age)
int(age) + 1
print("next year you will be", int(age)+1)
Gibson_Ek = int(input("How many students are learning there?"))

if Gibson_Ek > 108:
    print("That's too many students!")
elif Gibson_Ek > 90 and Gibson_Ek < 108:
    print("Just the right amount of students")
else:
    print("We can take more students")
