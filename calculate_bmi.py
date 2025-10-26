
def calculate_bmi(height, weight):
    print("Height = " + str(height))
    print("Weight = " + str(weight))
    bmi = weight / (height ** 2)
    print("BMI = " + str(bmi))

    # Determine BMI classification using conditional operators
    if bmi < 18.5:
        print("Weight Classification: Under Weight")
    elif bmi <= 25.0:
        print("Weight Classification: Normal Weight")
    else:
        print("Weight Classification: Over Weight")

calculate_bmi(weight=57, height=1.73)

print("\n--- Testing All Classifications ---")

print("\n1. Under Weight (BMI < 18.5):")
calculate_bmi(weight=50, height=1.73)

print("\n2. Normal Weight Boundary (BMI = 18.5):")
calculate_bmi(weight=55.37, height=1.73)

print("\n3. Normal Weight (18.5 ≤ BMI ≤ 25.0):")
calculate_bmi(weight=57, height=1.73)

print("\n4. Normal Weight Boundary (BMI = 25.0):")
calculate_bmi(weight=74.82, height=1.73)

print("\n5. Over Weight (BMI > 25.0):")
calculate_bmi(weight=80, height=1.73)
