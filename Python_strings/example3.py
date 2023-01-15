# Strin conversion Methods
# 1 capitalize()--> Returns a copy of the string with first character
# capitalized and rest of  the characters in lower case.

my_intro = 'my name raghav  i am from rajkot'
new_intro = my_intro.capitalize()
print(f" my new intro :{new_intro}")

# lower()and Upper() --method return the copy of string
# lower()and Upper() do not do any change in the original string itself
city = 'Bhopal'
new_city = city.lower()
print(f"my old city name was {city}")
print(f"my new city name is {new_city}")

new_city = city.upper()
print(f"my old city name was {city}")
print(f"my new city name is {new_city}")

# swapcase()-->Returns a copy of the string with the case of every
# character swapped . Means that lowercase characters
# are changed to uppercase and vice-versa.
name = 'Yogesh Pandey'
print(f"my old  name was {name}")
print(f'my name is {name.swapcase()}')

# title()-- Returns a copy of the string converted to proper case or
# title case. i.e. , all words begin with uppercase letter and
# the rest are in lowercase

text = "we got independence in 1947"
new_text = text.title()
print(f"Original text is {text}")
print(f"Title text is {new_text}")

text = "we celebrate the republic day on  janauary of year"
print(text.islower())
print(text.isupper())
print(text.istitle())

# isalpha() gives true only if string contain only aplhabet  gives Fasle
# even if it contains the spaces also

text = 'abcd   '
print(text.isalpha())

rollno = '0119cs181234'
print(rollno.isalnum())

# isdigit( )Returns True if the string contains only digits , otherwise
# returns False
print(rollno.isdigit())

# isspace( )->Returns True if the string contains only whitespace
# characters , otherwise returns False

str = "  "
print(str.isspace())

# startswith()--> return true string start with given character
city = 'Bhopal'
print(city.startswith('B'))
# endswith()--> return true if string ends with given character
print(city.endswith('l'))

# index()--> return the first index of given character if the any character more than once in the string
print(city.index('p'))
# if character is not present in the string then it raises  ValueError: substring not found
# print(city.index('e'))

# find()--> return the first index of given character if the any character more than once in the string
print(city.index('h'))
#if character is not present in the string then it gives -1
print(city.find('u'))

# replace( )
# Returns a copy of the string where all occurrences of a substring is
# replaced with another substring.

my_str='Hello'
print(f'original string is {my_str}')
# after replace
print(f'After replace string is {my_str.replace(my_str,"HI")}')


# Syntax:The replace() method takes three parameters:
# old->- old substring we want to replace
# new->- new substring which would replace the old substring
# count->(optional) - the number of times we want to replace the old substring with the new substring
#
# The replace() method returns a copy of the string where old substring is replaced with
# the new substring. Theoriginal string is unchanged.
# If the old substring is not found, it returns the copy of the original string.

stmt='Hello welcome to python once again welcome to python'
new_stmt=stmt.replace('welcome','world',1)
print(f'Original stmt is{stmt}')

print(f'After replace the stmt is {new_stmt}')

city='rajkot'
# if given substring is not found then it return the original string
new_city=city.replace('mt','nt')

print(new_city)