import openpyxl

z = openpyxl.Workbook()
ws = z.active

datas = ['EMPID', 'LNAME', 'FNAME', 'BDATE']
l1 =[ [1236, 'Smith', 'John', '05-01-1962'],
[2398, 'Adams', 'John', '03-22-1976'],
[4534, 'Johnson', 'Mary', '10-07-1971'],
[7834, 'Kirby', 'Frank', '05-27-1978'],
[9823, 'Harris', 'Kathy', '11-18-1982'],
[9875, 'Jones', 'Bill', '01-25-1953']
    ]
ws.append(datas)
for i in l1:
    row=i
    ws.append(row)
    # print(i)
# z.save("demo.xlsx")
