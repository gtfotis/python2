phonebook_dict = {
  'Alice': '703-493-1834',
  'Bob': '857-384-1234',
  'Elizabeth': '484-584-2923'
}
# This will print Alice's phone number
print("Alice's phone number is: " + phonebook_dict['Alice'])
print('----------------')
# This will add an entry to the dictionary
phonebook_dict['Kareem'] = '938-489-1234'
print(phonebook_dict)
print('----------------')
# This will delete Alice's phone entry
del phonebook_dict['Alice']
print(phonebook_dict)
print('----------------')
# This will change Bob's phone number
phonebook_dict['Bob'] = '968-345-2345'
print(phonebook_dict)
print('----------------')