# BMI Calculator - Internship Project 1

print("----- BMI CALCULATOR -----")

try:
    # Taking user input
    weight = float(input("Enter your weight in kilograms: "))
    height = float(input("Enter your height in meters: "))

    # Checking valid input
    if weight <= 0 or height <= 0:
        print("Weight and height must be positive numbers.")
    else:
        # BMI Formula
        bmi = weight / (height ** 2)

        # BMI Category
        if bmi < 18.5:
            category = "Underweight"
        elif bmi < 25:
            category = "Normal weight"
        elif bmi < 30:
            category = "Overweight"
        else:
            category = "Obese"

        # Display result
        print("\nYour BMI is:", round(bmi, 2))
        print("Category:", category)

except ValueError:
    print("Invalid input! Please enter numbers only.")
