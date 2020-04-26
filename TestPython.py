import numpy as np

#This project will be about multiple variable linear regresion

#Data inputs
data = np.array([[1,0],
                 [1,1],
                 [1,2],
                 [1,3],
                 [1,4],
                 [1,5]])

#Weight matricies for the weights
weight = np.array([[0.28],
                   [0.29]])

#Answer
answer = np.array([[0],
                   [10],
                   [20],
                   [30],
                   [40],
                   [50]])

#Learning Rate
Learningrate = .15


#(1/n)(answer-guess)^2
def changeWeights():
    guess = data.dot(weight)


    derivativei0 = 0
    derivativei1 = 0
    for x in range(6):
        derivativei0 += ((answer[x,0] - guess[x,0])*-data[x,0])
        derivativei1 += ((answer[x,0] - guess[x,0])*-data[x,1])

    derivativei0 = derivativei0/6
    derivativei1 = derivativei1/6

    weight[0,0] = weight[0,0] - (Learningrate*derivativei0)
    weight[1,0] = weight[1,0] - (Learningrate*derivativei1)








for x in range(1000):
    changeWeights()

new = np.array([[1,10],
                [1,100],
                [1,-10]])

print(new.dot(weight))                


print(weight)
