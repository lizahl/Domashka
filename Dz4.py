#Практика
#1
import random


names = ['james', 'tom', 'symon', 'frodo', 'sergey']
last_names = ['romanov', 'cash', 'black', 'white', 'blue']
people = []
random_name = 0
random_lastname = 0
for i in range(0,25):
	print(random.choice(names) + ' ' + random.choice(last_names))

#2

welcome = 'Welcome to California!'
country_list = 'USA, Ukraine, Russia, Italy, Spain'

country_list = country_list.split(', ')
print(country_list)
for i in range(0, len(country_list)):
	print(welcome[0:11]+country_list[i] + '!')

#3

cube = [x ** 3 for x in range(1000) if x % 2 != 0]
print(cube)

#4

s = [95, 60, 35, 135, 70, 250, 55, 73, 85, 40]
t = [2, 1, 1, 2, 1, 4, 1, 2, 1, 1]
v = [x / y for x in s for y in t if x / y > 50]
print(v)







