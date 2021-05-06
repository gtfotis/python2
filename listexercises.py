list_of_numbers = [23,3,54,20,2,45]
total = 0

# This is for finding the total

for number in list_of_numbers:
    print(str(total))
    total = total + number

# This is for finding the largest

largest = 0
for num in list_of_numbers:
    print("The current number is: " + str(num))
    print("The current LARGEST number is: " + str(largest))
    #If the CURRENT NUMBER is greater than the CURRENT LARGEST
    #Assign the value of CURRENT NUMBER to LARGEST
    if num > largest:
        largest = num

# This is for finding the smallest 

smallest = 0
for num in list_of_numbers:
    print("The current number is: " + str(num))
    print("The current SMALLEST number is: " + str(smallest))
    if num < smallest:
        smallest = num

# This is for finding even numbers

for num in list_of_numbers:
    if num % 2 == 0:
        print(num)





# print("The total is now: " + str(total))
# print("The total is also: " + str(sum(list_of_numbers)))
# print("The largest integer in this list is: " + str(max(list_of_numbers)))
# print("The smallest integer in this list is: " + str(min(list_of_numbers)))