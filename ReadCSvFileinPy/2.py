import csv

with open('employee.csv','r')as csv_file:
    csv_reader=csv.reader(csv_file)

    with open('new_emloyee.csv','w') as new_csv_file:
        csv_writer=csv.writer(new_csv_file)

        for line in csv_reader:
            csv_writer.writerow(line)