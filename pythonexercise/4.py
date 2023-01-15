import functools

emp_dict = {
    101: {'name': 'Anupriya Roy', 'depart_id': 1,
          'attendances':
              [{'date': 1, 'hours': [3.5, 4.5]},
               {'date': 2, 'hours': [3.2, 4.5]},
               {'date': 3, 'hours': [3.2, 4.6]},
               {'date': 4, 'hours': [3.0, 4.5]},
               {'date': 5, 'hours': [2.5, 4.5]},
               {'date': 6, 'hours': [1.5, 4.5]},
               {'date': 7, 'hours': [2, 3]},
               {'date': 8, 'hours': [0, 4.5]},
               {'date': 9, 'hours': [2, 3.5]},
               {'date': 10, 'hours': [4, 3.5]}
               ],
          'leaves':
              [{'date': 7, 'no_of_hours': 1.5},
               {'date': 70, 'no_of_hours': 1.5},
               {'date': 8, 'no_of_hours': 3}
               ]
          },
    102: {'name': 'Kadambari Sharma', 'depart_id': 1,
          'attendances':
              [
                  {'date': 1, 'hours': [0, 4.5]},
                  {'date': 2, 'hours': [3.2, 0]},
                  {'date': 3, 'hours': [3.2, 4.6]},
                  {'date': 4, 'hours': [1, 4.5]},
                  {'date': 5, 'hours': [2.5, 2]},
                  {'date': 6, 'hours': [1.5, 1]},
                  {'date': 7, 'hours': [2, 4]},
                  {'date': 8, 'hours': [1, 4.5]},
                  {'date': 9, 'hours': [2, 2]},
                  {'date': 10, 'hours': [2, 3.5]}
              ],
          'leaves':
              [
                  {'date': 1, 'no_of_hours': 3.5},
                  {'date': 2, 'no_of_hours': 2},
                  {'date': 2, 'no_of_hours': 2}
              ]
          },
    103: {'name': 'Abhishek Verma', 'depart_id': 1,
          'attendances':
              [
                  {'date': 3, 'hours': [3.2, 4.6]},
                  {'date': 4, 'hours': [1, 4.5]},
                  {'date': 5, 'hours': [2.5, 2]},
                  {'date': 6, 'hours': [1.5, 1]},
                  {'date': 7, 'hours': [2, 4]},
                  {'date': 8, 'hours': [1, 4.5]},
                  {'date': 9, 'hours': [2, 2]},
                  {'date': 10, 'hours': [2, 3.5]}
              ],
          'leaves':
              [
                  {'date': 1, 'no_of_hours': 3},
                  {'date': 2, 'no_of_hours': 2},
                  {'date': 2, 'no_of_hours': 3}
              ]
          }
}
for key in emp_dict.keys():
    sum_total_Attendance = 0
    for i in emp_dict.get(key).get('attendances'):
       sum_total_Attendance+=functools.reduce(lambda a,b:a+b,i.get('hours'))
    print("total attendance",sum_total_Attendance)


# print(emp_dict.get(101).get('attendances')[0].get('hours'))


emp_dict = {
    101: {'name': 'Anupriya Roy', 'depart_id': 1,
          'attendances':
              [{'date': 1, 'hours': [3.5, 4.5]},
               {'date': 2, 'hours': [3.2, 4.5]},
               {'date': 3, 'hours': [3.2, 4.6]},
               {'date': 4, 'hours': [3.0, 4.5]},
               {'date': 5, 'hours': [2.5, 4.5]},
               {'date': 6, 'hours': [1.5, 4.5]},
               {'date': 7, 'hours': [2, 3]},
               {'date': 8, 'hours': [0, 4.5]},
               {'date': 9, 'hours': [2, 3.5]},
               {'date': 10, 'hours': [4, 3.5]}
               ],
          'leaves':
              [{'date': 7, 'no_of_hours': 1.5},
               {'date': 70, 'no_of_hours': 1.5},
               {'date': 8, 'no_of_hours': 3}
               ]
          },
    102: {'name': 'Kadambari Sharma', 'depart_id': 1,
          'attendances':
              [
                  {'date': 1, 'hours': [0, 4.5]},
                  {'date': 2, 'hours': [3.2, 0]},
                  {'date': 3, 'hours': [3.2, 4.6]},
                  {'date': 4, 'hours': [1, 4.5]},
                  {'date': 5, 'hours': [2.5, 2]},
                  {'date': 6, 'hours': [1.5, 1]},
                  {'date': 7, 'hours': [2, 4]},
                  {'date': 8, 'hours': [1, 4.5]},
                  {'date': 9, 'hours': [2, 2]},
                  {'date': 10, 'hours': [2, 3.5]}
              ],
          'leaves':
              [
                  {'date': 1, 'no_of_hours': 3.5},
                  {'date': 2, 'no_of_hours': 2},
                  {'date': 2, 'no_of_hours': 2}
              ]
          },
    103: {'name': 'Abhishek Verma', 'depart_id': 1,
          'attendances':
              [
                  {'date': 3, 'hours': [3.2, 4.6]},
                  {'date': 4, 'hours': [1, 4.5]},
                  {'date': 5, 'hours': [2.5, 2]},
                  {'date': 6, 'hours': [1.5, 1]},
                  {'date': 7, 'hours': [2, 4]},
                  {'date': 8, 'hours': [1, 4.5]},
                  {'date': 9, 'hours': [2, 2]},
                  {'date': 10, 'hours': [2, 3.5]}
              ],
          'leaves':
              [
                  {'date': 1, 'no_of_hours': 3},
                  {'date': 2, 'no_of_hours': 2},
                  {'date': 2, 'no_of_hours': 3}
              ]
          }
}

# Find the following outputs - Don’t use a loop. The only loop that will be used is the main dictionary loop of emp_dict
# Employee's total attendance and leave hours :
# [
# {'employee_id': 101, 'employee_name':'Anupriya Roy','total_attendance_hours': 66.5, 'total_leave_days': 6.0},
# {'employee_id': 102,,'employee_name':'Kadambari Sharma', 'total_attendance_hours': 49.0, 'total_leave`_days': 7.5},
# {'employee_id': 103,'employee_name':'Abhishek Verma', 'total_attendance_hours': 41.3, 'total_leave_days': 8}
# ]
