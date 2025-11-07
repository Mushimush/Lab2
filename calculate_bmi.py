# Function to calculate BMI and determine weight classification.
# Parameters:
# height: Height in meters
# weight: Weight in kilograms
# Returns:
# -1 if underweight, 0 if normal weight, 1 if overweight.

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
