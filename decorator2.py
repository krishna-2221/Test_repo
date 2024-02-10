
def isValid(func):
    age=1

    def inner():
        if age>=18:
            func()
        else:
            print("You are not eligible for voting")
    return inner

@isValid
def vote():
    print("You are eligible to vote")
vote()