import random
numDarts = int (input("Enter the number of darts to throw: "))
distanceInCircle = 0
count = 0
while count<numDarts:
    x = random.uniform(-1,1)
    y = random.uniform(-1,1)
    distance = x**2 + y**2
    if distance <= 1:
        distanceInCircle += 1
    count += 1
approxPi = 4 *(distanceInCircle/numDarts)
print("The approximate pi is " ,approxPi)