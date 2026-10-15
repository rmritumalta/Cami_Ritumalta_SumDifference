num1 = int(input("Enter a number to add: "))
num2 = int(input("Enter another number to add: "))
sum = 0
difference = 0

def calculate_sum():
    global sum
    sum = num1 + num2
    print("The sum is: ", sum)

def calculate_difference():
    global difference
    difference = num1 - num2
    print("The difference is: ", difference)

calculate_sum()
calculate_difference()