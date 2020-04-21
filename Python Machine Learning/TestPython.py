import random

#This Project will be a machine learning Project which will see if a random point is eithier above or below the line of y = 50
#It Will use the simple perceptron neural Network

#initalize weights
weight = []

#Bias
weight.append(random.random())
#Weight
weight.append(random.random())

#Learning Rate
learningRate = .1

#Update weight from this formula w1 = w1 + (target-guess)y1
def updateWeight(inputy):
    #Guess is created by combining all weights with inputs and adding the bias
    guess = (weight[1]*inputy) + weight[0]

    #Activation function
    if(guess >= 0):
        guess = 1
    else:
        guess = 0

    answer = 0
    #The answer is calculated
    if(inputy>=50):
        answer = 1
    else:
        answer = 0

    #Updates the weight
    weight[1] = weight[1] + (.1*(answer - guess)*inputy)
    weight[0] = weight[0] + (.1*(answer-guess))

#Sees For User how well it is doing
def guess(inputy):
    guess = weight[1]*inputy + weight[0]
    if(guess >= 0):
        print("Above Line")
    else:
        print("Below Line")


#Training
for x in range(1,10000):
    rnumy = random.randrange(0,100)
    updateWeight(rnumy)

print(weight)
guess(50)
guess(49)
