print("===================================")
print("        BMI CALCULATOR")
print("===================================")
while True:
    # Get weight
    try:
        weight = float(input("\nEnter your weight in kg: "))
        if weight < 0:
            print("Error: Weight cannot be negative.")
            continue
    except ValueError:
        print("Error: Please enter a valid number for weight.")
        continue
    # Get height
    try:
        height = float(input("Enter your height in meters: "))
        if height < 0:
            print("Error: Height cannot be negative.")
            continue
        if height == 0:
            print("Error: Height cannot be zero.")
            continue
    except ValueError:
        print("Error: Please enter a valid number for height.")
        continue
    # Calculate BMI
    bmi = weight / (height * height)
    # Determine BMI category
    if bmi < 18.5:
        category = "Underweight"
    elif bmi < 25:
        category = "Normal"
    elif bmi < 30:
        category = "Overweight"
    else:
        category = "Obese"
    # Display result
    print("\n-----------------------------------")
    print("BMI:", round(bmi, 2))
    print("Category:", category)
    print("-----------------------------------")
    # Ask whether to calculate again
    again = input("\nCalculate BMI again? (Y/N): ")
    if again.lower() != "y":
        print("\nThank you for using BMI Calculator!")
        break
