# [2,4,5],[4,6,8],[3,6,9]]
# Considering the above list, we need to have a sum of all the values of all the inner lists.
# Find the sum of only even numbers
# Find the sum of all the numbers from all the inner lists
# Don’t use a loop, use lambda, filter, map, zip whichever is possible
import functools

my_new_list = [[2, 4, 5], [4, 6, 8], [3, 6, 9]]

sum_inner_list = functools.reduce(lambda a, b: a + b, functools.reduce(lambda a, b: a + b, my_new_list))
# first we arer getting all the element of innerlist
# then again applying the reduce to calculate sum
print(functools.reduce(lambda a, b: a + b, my_new_list))
print(sum_inner_list)

even_nos_sum = functools.reduce(lambda a, b: a + b,
                                filter(lambda a: a % 2 == 0, functools.reduce(lambda a, b: a + b, my_new_list)))
# first we arer getting all the element of innerlist
# then filtering the even nos only
# then again applying the reduce to calculate the sum
print(even_nos_sum)


