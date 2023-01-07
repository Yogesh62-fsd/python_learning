i=0
while i<10:
    i=i+1
    if(i%2!=0):#if condition true then rest of the line after the continue will not execute
        continue
    print(i)
#---------------------------------------------
s=input('enter the name')
size=len(s)
i=0
while i<size:
    if(s[i]=="a"or s[i]=="e"or s[i]=="i" or s[i]=="o" or s[i]=="u"):
      continue
i=i+1
print(s[i])
#----------------------
total=0
while(True):
  no=  eval(input('enter the no and press 0 to stop:'))
  if no<0: continue
  total+=no
  if no==0 :
      break
print("Sum of total {0}".format(total))
