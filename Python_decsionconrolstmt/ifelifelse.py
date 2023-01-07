ch=input('enter any character or digit or special symbols:')
if(ch>="A" and ch<="Z"):
    print('Character is Capital letter.')
elif(ch>="a" and ch<="z"):
    print('Character is Small letter.')
elif(ch>="0" and ch<="9" ):
    print('Character is digit.')
else:
    print('Character is special symbols>')