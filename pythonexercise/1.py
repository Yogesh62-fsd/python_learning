# Take a list of integers. Take a dictionary. Iterate through the dictionary and check if values from the list
# match the value in the dictionary and create a new list. Whichever value is not found in the dictionary,
# skip that and don’t append in the new list

my_list=[22,41,26,37,18,34,90,67,25]
my_dict={"1":45,"2":56,"3":34,"4":18,"5":26,"6":22,"7":42,"8":78,"9":14}
my_new_list=[]
for key,val in my_dict.items():
    if val in my_list:
        my_new_list.append(val)
print(my_dict.values())
print(my_new_list)


























