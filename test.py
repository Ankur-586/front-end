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

import pandas as pd

employee_list = [{'Full Name': 'Audrey Miller', 'Username': 'audrey', 'Department': 'Development'}, {'Full Name': 'Arden Garcia', 'Username': 'ardeng', 'Department': 'Sales'}, {'Full Name': 'Bailey Thomas', 'Username': 'baileyt', 'Department': 'Human Resources'}, {'Full Name': 'Blake Sousa', 'Username': 'sousa', 'Department': 'IT infrastructure'}, {'Full Name': 'Cameron Nguyen', 'Username': 'nguyen', 'Department': 'Marketing'}, {'Full Name': 'Charlie Grey', 'Username': 'greyc', 'Department': 'Development'}, {'Full Name': 'Chris Black', 'Username': 'chrisb', 'Department': 'User Experience Research'}, {'Full Name': 'Courtney Silva', 'Username': 'silva', 'Department': 'IT infrastructure'}, {'Full Name': 'Darcy Johnsonn', 'Username': 'darcy', 'Department': 'IT infrastructure'}, {'Full Name': 'Elliot Lamb', 'Username': 'elliotl', 'Department': 'Development'}, {'Full Name': 'Emery Halls', 'Username': 'halls', 'Department': 'Sales'}, {'Full Name': 'Flynn McMillan', 'Username': 'flynn', 'Department': 'Marketing'}, {'Full Name': 'Harley Klose', 'Username': 'harley', 'Department': 'Human Resources'}, {'Full Name': 'Jean May Coy', 'Username': 'jeanm', 'Department': 'Vendor operations'}, {'Full Name': 'Kay Stevens', 'Username': 'kstev', 'Department': 'Sales'}, {'Full Name': 'Lio Nelson', 'Username': 'lion', 'Department': 'User Experience Research'}, {'Full Name': 'Logan Tillas', 'Username': 'tillas', 'Department': 'Vendor operations'}, {'Full Name': 'Micah Lopes', 'Username': 'micah', 'Department': 'Development'}, {'Full Name': 'Sol Mansi', 'Username': 'solm', 'Department': 'IT infrastructure'}]

df = pd.DataFrame(employee_list)
print(df)

# for employee in employee_list:
#     emp_str = employee
    

# with open ('employee_list.csv', 'w') as file:
    #     file.write(str(employee))