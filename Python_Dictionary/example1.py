# Python Dictionary is unordered collection which store the data in the form of key-value pair.
# syntax {key:value,key-value}
# While values can be of any data type and can repeat, but keys must be of immutable type and must be unique
my_details = {"name": "yogesh", "age": 23, "per": 89.79}
print(my_details)
# for same key more 1 value is given it overwrite the previous values
my_details={"name": "yogesh", "age": 23, "per": 89.79,"name":"praveen pandey"}
print(my_details)

# key is integer
my_dict={1:"Python",2:"Java",3:"Javasscript"}
print(my_dict)
# some time value can be list or it may be collection also
my_dict_={"cs":['python','java'],"EE":['AcGEN','IndMotor'],"Me":['Autocad','LatheMachn']}
print(my_dict_)

# They can be nested.
# They are mutable.
# They are dynamic.
# They are unordered.
# Unlike Lists and tuples , a dictionary item is accessed by it’s corresponding key not index

# acccessing key
for i in my_dict_:
    print(i)
keys=my_dict.keys()
print(keys)
for i in range(len(my_details)):
    print(i)
# accessing values
my_values=my_dict.values()
print(my_values)
# Accessing individual element.
my_details = {"name": "yogesh", "age": 23, "per": 89.79}
my_dict_val=my_details.get("name")
print(my_dict_val)
print("--------------------------------------")
my_dict={1:"Python",2:"Java",3:"Javasscript"}
my_dict_val2=my_dict[2]
# [2] represent the key not the index
print(my_dict_val2)

my_car = {"company":"Mercedes","year":1978,"country":"Germany"}
print(my_car["company"])

# so element we can get values by [] and get()
# [] gives key error when key is not found
# print(my_car["brand"])
# # whereas get() gives keyError
# print(my_car["brand"])


my_dicts={'a':[1,2,3,4,5],'b':(2,3,4,5)}
print(my_dicts)
my_dicts["a"]=[10,2,3,4,5]
my_dicts["b"]=(10,20,30,40)
print(my_dicts)









