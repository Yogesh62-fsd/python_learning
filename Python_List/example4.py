# modifying the list
# adding the new element
sports = ['cricket', 'football', 'tennis', 'volleyball', 'hockey']
sports[4] = 'rubgy'
print(sports)

# it will generate error
# sports[5]='Tabletennis'
# print(sports)

sports = ['cricket', 'football', 'tennis', 'volleyball', 'hockey']
del sports[4]
print(sports)
print("---------------------------------------------------------------------")
# Deleting multiple elements by assigning empty list to slice operator.
sports = ['cricket', 'football', 'tennis', 'volleyball']
print(sports)
sports[1:4] = []
print(sports)
print("---------------------------------------------------------------------")
# # Deleting multiple elements by passing slice to del operator.
# it will remove the element from start to end-1
sports = ['cricket', 'football', 'tennis', 'volleyball', 'hockey']
del sports[1:3]
print(sports)
del sports[0:4]
print(sports)
print("---------------------------------------------------------------------")

# Deleting the entire list
sports = ['cricket', 'football', 'tennis', 'volleyball', 'hockey']
del sports
# now sports list has been deleted but if we try to print it then we will get Name error
# print(sports)

print("---------------------------------------------------------------------")
# Merging 2 list
sports = ['cricket', 'football', 'tennis', 'volleyball', 'hockey']
games = ['kho-kho', 'khabbdi', 'ice-water']
allgamessports = sports + games
print(allgamessports)

indoor_games=['Ludo','chess','carrom']+allgamessports
print(indoor_games)

# it will generate error
# slist=indoor_games+"snake-ladder"
# print(slist)

evens=[2,4,6]
evens=[8]+evens+[10]
print(evens)

cars=['hondacity','creta','jeep','ciaz']
cars=cars+['ertiga']
print(cars)
# list() takes the string and add the letter of string as  individual element  to the list.
cars=cars+list("breza")
print(cars)

# Multiplying the List
listnos=[2,4,8,0]
listnos=listnos*3
print(listnos)

# listnos=listnos*4.0
# print(listnos) can't multiply sequence to non-type int type list.
#
# cars=["ciaz","jeep,","breza"]
# cars=cars*["ertiga"]
# print(cars)

# Membership Operator On List
sports = ['cricket', 'football', 'tennis', 'volleyball', 'hockey']
print('cricket' in sports)
print('kho-kho' in sports)
print('khabbdi' not in sports)