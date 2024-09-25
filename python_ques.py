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



# def to_seconds(hours, minutes, seconds):
#     return hours*3600+minutes*60+seconds

# print("Welcome to this time converter")

# cont = "y"
# while(cont.lower() == "y"):
#     hours = int(input("Enter the number of hours: "))
#     minutes = int(input("Enter the number of minutes: "))
#     seconds = int(input("Enter the number of seconds: "))

#     print("That's {} seconds".format(to_seconds(hours, minutes, seconds)))
#     print()
#     cont = input("Do you want to do another conversion? [y to continue] ")
    
# print("Goodbye!")

# Dear Mrs. Nisha Madam

# I would like to inform you that I am resigning from my position as System Analyst, effective 04-04-2024.

# Thank you for all the support and opportunities you have provided me over the years. I have truly enjoyed my time working at Leads Next Tech and am grateful for the encouragement you have given me to pursue my personal and professional development.
# I will do everything I can to complete my current projects and train other team members or new employees to take over my duties. Please let me know if there is anything else I can do to help during this transition period.
# I wish the company continued success in the future and hope to stay in touch.

# Sincerely,
# Ankur

# Fibonacci Numbers using Native Approach
# n = 10
# num1 = 0
# num2 = 1
# next_number = num2  
# count = 1

# while count <= n:
#     print(next_number, end=" ")
#     count += 1
#     # print(num1, num2, next_number)e  
#     num1, num2 = num2, next_number
#     next_number = num1 + num2
# print()

# Find the number of occurrences of a character in a String?
s = 'abbssea'
s = {}
for i in range(len(s)-1):
    c = s[i]
    if s[i+1] == c:
        s[c] += 1
    else:
        s[c] = 2  # Start count at 2 since we found it twice

for char, count in s.items():
    print(f"{char}: {count}")