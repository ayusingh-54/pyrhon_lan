print("Welcome to the BMI Calculator")
waight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in m: "))
bmi = waight / (height*height)
print(int(bmi))
print(round(bmi , 2))