height = float(input("Enter your height in"))
weight = float(input("Enter your weight in kg"))
bmi = weight / (height ** 2)
if bmi < 18.5:
    print("You are underweight")
elif 18.5 <= bmi < 25:
    print("You are normal weight")
elif 25 <= bmi < 28:
    print("You are overweight")
elif 28 <= bmi <= 32:
    print('You are obese')
elif bmi > 32:
    print('You are severely obese')