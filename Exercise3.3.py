def check_hemoglobin_value(gender, hemoglobin):
    if gender == "female":
        if hemoglobin < 117:
            print("Low hemoglobin value for adult females.")
        elif hemoglobin >= 117 and hemoglobin <= 155:
            print("Normal hemoglobin value for adult females.")
        else:
            print("High hemoglobin value for adult females.")
    elif gender == "male":
        if hemoglobin < 134:
            print("Low hemoglobin value for adult males.")
        elif hemoglobin >= 134 and hemoglobin <= 167:
            print("Normal hemoglobin value for adult males.")
        else:
            print("High hemoglobin value for adult males.")
    else:
        print("Invalid gender.")


gender = input("Enter your biological gender (male or female): ")
hemoglobin_value = float(input("Enter your hemoglobin value (g/l): "))


check_hemoglobin_value(gender, hemoglobin_value)