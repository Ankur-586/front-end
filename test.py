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
print(x)
    
import os 

outputs = {}
outputs['current_directory_before'] = os.getcwd()
print(os.listdir())