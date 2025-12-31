weight=float(input("Enter your weight in kg = "))
height=float(input("Enter your height in cm = "))
bmi=weight/(height/100)**2
print("Your BMI is =",bmi)
if bmi<=18.5:
    print("Your are Underweight")
elif bmi<=24.9:
    print("you are normal")
elif bmi<=29.9:
    print("Your are overweight")
elif bmi<=34.9:
    print("you are severly overweight")
elif bmi<=39.9:
    print("Your are obese")
else:
    print("you are severly obese")