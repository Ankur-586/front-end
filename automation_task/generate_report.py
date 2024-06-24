'''
Task:
Imagine you are an IT Specialist at a medium-sized company. The Human Resources Department at your 
company wants you to find out how many people are in each department. You need to write a Python 
script that reads a CSV file containing a list of the employees in the organization, counts how 
many people are in each department, and then generates a report using this information. 
The output of this script will be a plain text file.
'''
import csv

def read_employees(csv_file):
    csv.register_dialect('empDialect', skipinitialspace=True, strict=True)
    employee_file = csv.DictReader(open(csv_file), dialect = 'empDialect')
    employee_list = []
    for data in employee_file:
        employee_list.append(dict(data))    
    return employee_list

def process_data(emp_data_list):
    department_list = []
    for employee_data in emp_data_list:
        department_list.append(employee_data['Department'])
        
    department_data = {}
    for department_name in set(department_list):
        department_data[department_name] = department_list.count(department_name)
    return department_data

def write_report(dictionary,report_file):
    with open(report_file, "w") as f:
        for k in sorted(dictionary):
            f.write(str(k) + ':' + str(dictionary[k]) + '\n')
        f.close()

csv_file_location = r'D:\front-end\automation_task\employee_list_plain.csv'
report_file_location = 'report.txt'

emp_data = read_employees(csv_file_location)
process_emp_data = process_data(emp_data)
report_emp_data = write_report(process_emp_data,report_file_location)
print(emp_data)