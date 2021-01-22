###Password Generator
import random
lenght=int(input('Enter the lenght of the Password to be generated :'))
password=''
for i in range (lenght) :
    n=random.randint(35,125)
    password+=chr(n)
print(f'Your Password is :{password}')
