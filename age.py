#criteria section
def classify_age(age):
    if age < 0:
        print("Invalid age. Please try again.")
    elif age <= 12:
        print("Child")
    elif age <= 19:
        print("Teen")
    elif age <= 64:
        print("Adult")
    else:
        print("Senior")

#input section
def inp():
    response = int(input("Enter age: "))
    classify_age(response)

#start
inp()

#loop section
while True:
    contq = input("Got any more age to classify? Y/N >> ")
    if contq == "Y":
        inp()
    else:
        print("Ok, bye.")
        break