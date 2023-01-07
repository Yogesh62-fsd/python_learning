year=eval(input('enter the year '))
leap=True
if year%4==0:
    if year%100==0:
         if year%400==0:
             print('It is Leap Year',year)
         else:
            print('It is Not Leap Year',year)
    else:
        print('It is Leap Year', year)
else:
    print('It is Not Leap Year',year)