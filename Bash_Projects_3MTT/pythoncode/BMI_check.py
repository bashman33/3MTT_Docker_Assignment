# Write a program that interprtes the Body Mass Index(BMI) based on a user's weight and Height
# Under 18.5 they are Underweight, over 18.5 but below 25 they have a normal weight
# Over 25 but below 30 they are Overweight, Over 30 but below 35 they are Obese
# Above 35 they are Clinically Obese.

height = float(input("Enter your height in M:   "))
weight = float(input("Enter your weight in Kg:  ")) 
BMI = round(weight/height**2)
BMI_float = (BMI)
if BMI_float < 18.5:
    print(f"Your BMI is {BMI_float}, You are Underweight.")
elif BMI_float <25:
    print(f"Your BMI is {BMI_float}, You have a Normal weight")
elif BMI_float <30:
    print(f"Your BMI is {BMI_float}, You are Overweight")
elif BMI_float <35:
    print(f"Your BMI is {BMI_float}, You are Obese")
else:
    print(f"Your BMI is {BMI_float}, You are Clinically Obese")