meal = {
    "entree": "grilled chicken",
    "drink": "lime la croix",
    "side": "steamed kale",
    "dessert": "ice cream"
}

# print(meal["side"])
# print("Tonight I will have %s for dinner with %s on the side." % (meal["entree"], meal["side"]))

# # IF the key "dessert" is found in the dictionary meal
# # THEN print the first statement
# # IF NOT, THEN print the second statement
# if "dessert" in meal:
#     print("OF COURSE Sean had dessert!! He had %s." % (meal["dessert"]))
# else: 
#     print("Sean did NOT have dessert and now he is sad. :(")

# READ what is in our meal
print(meal)
# CREATE a NEW key called "appetizer" with the value "bacon"
meal["appetizer"] = "bacon"
# Update the key "drink", with the value "sweet tea"
meal["drink"] = "sweet tea"
# Delete an entry by referencing its key
del meal["dessert"]
print(meal)