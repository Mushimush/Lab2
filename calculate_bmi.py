
def calculate_bmi(height, weight):
    print("Height = " + str(height))
    print("Weight = " + str(weight))
    bmi = weight / (height ** 2)
    print("BMI = " + str(bmi))

    # Determine BMI classification using conditional operators
    if bmi < 18.5:
        print("Weight Classification: Under Weight")
        return -1
    elif bmi <= 25.0:
        print("Weight Classification: Normal Weight")
        return 0
    else:
        print("Weight Classification: Over Weight")
        return 1

