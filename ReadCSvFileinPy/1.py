import csv

with open('employee.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)

    for line in csv_reader:
        if (line != '\t'):
            print(line)
# # l1=[1236, 'Smith', 'John', '05-01-1962']
# # l2=[2398, 'Adams', 'John', '03-22-1976']
# # l3=[4534, 'Johnson', 'Mary','10-07-1971']
# # l4=[7834,'Kirby', 'Frank', '05-27-1978']
# # l5=[9823, 'Harris', 'Kathy', '11-18-1982']