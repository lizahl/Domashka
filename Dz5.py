
#Zip

#1zip

>>> name = ['John', 'Naomi', 'Willis', 'Helen', 'Cory', 'Amice', 'Robert']
>>> secname = ['Darren', 'Valerie', 'Gerald', 'Betty', 'Curtis', 'Sophia', 'Matthew']
>>> surname = ['Lucas', 'Francis', 'Hardy', 'Lyons', 'Mathews', 'Gray', 'Harrington']
>>> zipped = zip(name, secname, surname)  
>>> list(zipped)

#2zip

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
numbers = [1, 2, 3, 4, 5, 6, 7]

result = zip(letters, numbers)
result_list = list(result)
print(result_list)

l, n =  zip(*result_list)
print('l =', l)
print('n =', n)



#FIZZBUZZ

f = int(input('enter Fizz:' ' '))
b = int(input('enter Buzz:' ' '))
n = int(input('enter Number:' ' '))
FB = list(map(lambda x: 'Fizz'*(x % f == 0) + 'Buzz'*(x % b == 0) or x, range(1, n)))
print(FB)


#Practika
#1

def my_listup(S):
    return S.upper()

S = 'aaAaaaAaaAAAAaa  jusT Help'


def my_listlow(S):
    return S.lower()

S = 'aaAaaaAaaaaaa Help'

lowerst = tuple(map(my_listlow, S))

print(lowerst)


upperst = tuple(map(my_listup, S))

print(upperst)


