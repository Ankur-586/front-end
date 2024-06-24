employee_list = [
    {'Full Name': 'Audrey Miller', 'Username': 'audrey', 'Department': 'Development'},
    {'Full Name': 'Arden Garcia', 'Username': 'ardeng', 'Department': 'Sales'},
    {'Full Name': 'Bailey Thomas', 'Username': 'baileyt', 'Department': 'Human Resources'},
    {'Full Name': 'Blake Sousa', 'Username': 'sousa', 'Department': 'IT infrastructure'},
    {'Full Name': 'Cameron Nguyen', 'Username': 'nguyen', 'Department': 'Marketing'},
    {'Full Name': 'Charlie Grey', 'Username': 'greyc', 'Department': 'Development'},
    {'Full Name': 'Chris Black', 'Username': 'chrisb', 'Department': 'User Experience Research'},
    {'Full Name': 'Courtney Silva', 'Username': 'silva', 'Department': 'IT infrastructure'},
    {'Full Name': 'Darcy Johnsonn', 'Username': 'darcy', 'Department': 'IT infrastructure'},
    {'Full Name': 'Elliot Lamb', 'Username': 'elliotl', 'Department': 'Development'},
    {'Full Name': 'Emery Halls', 'Username': 'halls', 'Department': 'Sales'},
    {'Full Name': 'Flynn McMillan', 'Username': 'flynn', 'Department': 'Marketing'},
    {'Full Name': 'Harley Klose', 'Username': 'harley', 'Department': 'Human Resources'},
    {'Full Name': 'Jean May Coy', 'Username': 'jeanm', 'Department': 'Vendor operations'},
    {'Full Name': 'Kay Stevens', 'Username': 'kstev', 'Department': 'Sales'},
    {'Full Name': 'Lio Nelson', 'Username': 'lion', 'Department': 'User Experience Research'},
    {'Full Name': 'Logan Tillas', 'Username': 'tillas', 'Department': 'Vendor operations'},
    {'Full Name': 'Micah Lopes', 'Username': 'micah', 'Department': 'Development'},
    {'Full Name': 'Sol Mansi', 'Username': 'solm', 'Department': 'IT infrastructure'}
]

import pandas as pd
def raw_file_to_csv_using_pandas(employee_list):
    df = pd.DataFrame(employee_list)
    with open ('employee_list.csv', 'w') as file:
        file.write(str(df))

def raw_file_to_csv_using_plain_python(employee_list):
    s_no = 1
    column_names = 'S.No, FullName, Username, Department\n'
    data = column_names
    for employee in employee_list:
        FullName , Username , Department = employee['Full Name'] , employee['Username'] , employee['Department']
        csv_rows = f"{s_no}, {FullName} , {Username} , {Department}\n"
        data += csv_rows
        s_no += 1
    with open('employee_list_plain.csv', 'w') as file:
        file.write(data)

raw_file_to_csv_using_plain_python(employee_list)
