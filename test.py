# a = 'Nun'
# result = ''.join(list(a)[::-1])
# if a == result:
#     print(True)
# else:
#     print(False)

# https://www.keka.com/javascript-coding-interview-questions-and-answers

# l = [1,2,3,4,5]
# for i in range(len(l)-1):
#     print(i)
# #   VS 
# l = [1, 2, 3, 4, 5]
# for i in range(len(l)-1):
#     print(l[i+1])
    
# x = "Hello" + 5
# print(x)

# num = 6
# for i in range(2, num):
#     if not num % i == 0:
#         break
#     else:
#         print('prime')

l = [[1,3],[4,2]]

s = ''
for i in l:
    for j in i:
        s = s + str(j)
x = list(s)
# print(max(x),x)

# fibo
num = 10
num_1 = 0
num_2 = 1
for i in range(10):
    x = num_1 + num_2
# print(x)
    
import os 

outputs = {}
outputs['current_directory_before'] = os.getcwd()
# print(os.listdir())

log = "July 31 07:51:48 mycomputer bad_process[12345]: ERROR Performing package upgrade"
index = log.index("[")
# print(log[index+1:index+6])

import re
log = "July 31 07:51:48 mycomputer bad_process[12345]: ERROR Performing package upgrade"
regex = r"\[(\d+)\]"
result = re.search(regex, log)
# print(result[1])

import re
# s = 'qwertycatsfruits'
# print(re.search(r'fruits$',s))
# print(re.search(r"p.ng", "Pangaea", re.IGNORECASE)) 

# Create a regex that finds dates in the format MM/DD/YY or MM/DD/YYYY and returns just the year part.
s = '06-06-2024'
#print('this one:',re.search(r'(\b\d{2}[/-]\d{2}[/-](\d{2}|\d{4})\b)',s))

s = '+91 8884 154409'
indian_pattern_mobile = re.search(r"\d{4} \d{6}",s)
# print(indian_pattern_mobile) 



import csv

def read_employees(csv_file):
    csv.register_dialect('empDialect', skipinitialspace=True, strict=True)
    employee_file = csv.DictReader(open(csv_file), dialect = 'empDialect')
    employee_list = []
    for data in employee_file:
        employee_list.append(dict(data))    
    return employee_list

def count_dept(emp_data_list):
    department_list = []
    for data in emp_data_list:
        department_list.append(data['Department'])
    count_dict = {}
    for dept in sorted(department_list):
        count_dict[dept] = department_list.count(dept)
    return count_dict
    
csv_file_location = r'D:\front-end\automation_task\employee_list_plain.csv'
emp_data = read_employees(csv_file_location)
process_emp_data = count_dept(emp_data)
print(process_emp_data)