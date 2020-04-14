import random
def getAnswer(answerNum):
    if answerNum == 1:
        return ("it is certain")
    else:
        for i in range (2,10):
            return ("yes")
print(getAnswer(random.randint(1,9)))