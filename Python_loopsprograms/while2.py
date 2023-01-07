i=1
while i<10:
      print(i)
      if(i==5):
       break
      i=i+1
else:
   print('Done with printing nos')
#--------------------------
mylist=['grapes','papaya','pineapple','apple','mango']
i=0
size=len(mylist)
while i<size:
      if mylist[i] =='mango' :
        print('Mango found')
        break
      i=i+1
else:
  print('Mango not found')
#---------------------------------------------
# s=input('enter your name')
# i=0
# size=len(s)
# while i<size:
#     if s[i] =='a'or s[i] =='e'or s[i] =='i' or s[i] =='o' or s[i] =='u':
#         print("Name {0}  contains the vowel".format(s))
#         break
#         # print(s[i])
#     i=i+1
# else:
#     print("Name {0} not contains any vowel".format(s))