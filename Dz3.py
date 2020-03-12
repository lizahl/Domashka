#1.

num = [4, 6, 8, 45, 32, 78, 90, 32, 9, 17]
sum = 0
for i in num:
    sum += i
print(sum)

#2.

num = [4, 6, 8, 45, 32, 78, 90, 32, 9, 17]
sum = 0
i = 0
while i <= len(num):
    for i in num:
        sum += i
print(sum)

#3.
'''
import sys
filename = sys.argv[1]
f=open(filename, 'r')
file_list=[]
for line in f:
    file_list.append(line)
f.close()
file_list.reverse()
print(file_list)
for i in range(0, len(file_list)):
    print(file_list[i])
'''

#4

amount = int(input('PLEASE ENTER AMOUNT Multiple of $ 5.0 LIMIT: $ 800' '\n'))
money_list = [500, 100, 50, 20, 10, 5]
banknote = {500: '0', 100: '0', 50: '0', 20: '0', 10: '0', 5: '0'}


if (amount % 5 != 0) or (amount > 800):
	print('ENTER ANOTHER AMOUNT')

elif amount > 0:
    for x in money_list:
        if (amount // x) > 0:
            result = amount // x
            banknote[x] = result
            amount -= result * x
print(f"""
500 : {banknote[500]},
100 : {banknote[100]},
50 : {banknote[50]}, 
20 : {banknote[20]},
10 : {banknote[10]},
5 : {banknote[5]} """)

