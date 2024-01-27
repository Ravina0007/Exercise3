#program that asks a fisher the length of a zander in centimeters

size_limit = 42

def check_zander_length(length):
    if length >= size_limit:
        print("Congratulations! The zander meets the size limit.")
    else:
        difference = size_limit - length
        print("The zander is below the size limit. Please release the fish back into the lake.")
        print(f"The zander is {difference} centimeters below the size limit.")


length = float(input("Enter the length of the zander in centimeters: "))
check_zander_length(length)