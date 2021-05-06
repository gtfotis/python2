jujutsu_sorcerers = []
jujutsu_sorcerers.append("Itadori")
jujutsu_sorcerers.append("Fushiguro")
jujutsu_sorcerers.append("Kugisaki")
jujutsu_sorcerers.append("Inumaki")
jujutsu_sorcerers.append("Gojo")

# print(jujutsu_sorcerers)

index = 0

# print(len(jujutsu_sorcerers))
# Here is my WHILE loop
# It has a start at index 
# and finishesat the end of the list
print("-----WHILE LOOP-----")
while index < len(jujutsu_sorcerers):
    print(jujutsu_sorcerers[index])
    index = index + 1

print("-----FOR LOOP-----")
# Here is a FOR loop
for sorcerer in jujutsu_sorcerers:
    print(sorcerer)

# FOR every SINGLE ITEM, which I am calling "sorcerer",
# that exists in my COLLECTION OF ITEMS, called "jujutsu_sorcerers"
# PRINT that SINGLE ITEM'S VALUE