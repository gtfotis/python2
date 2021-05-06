title = "Jujutsu Sorcerers"
# STOP = 10
counter = 0

while counter < len(title):
    print("The counter value is: " + str(counter))
    # IF the value of counter is an EVEN number 
    # AND if the character is NOT BLANK
    # THEN print the character at that index
    if (counter % 2) == 0 and title[counter] != " ":
        print(title[counter])
    counter = counter + 1