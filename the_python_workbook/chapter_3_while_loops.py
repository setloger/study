# exercise 63
from typing import Collection


list_numbers = []
number = int(input("Enter a number.:"))
"""if list_numbers == 0 and  number == 0 : 
    print(f'You entered is {number}. It\'s no OK! Try again!')
    
else:"""
while number !=0:
    list_numbers.append(number)
    print(f'You added: {number}, to calculate the average')
    number = int(input("Enter a number.:"))
mean = sum(list_numbers)/len(list_numbers)
print(f'Average of numbers is {mean}')

# exercise 64
price_sheet = [4.95, 9.95, 14.95, 19.95, 24.95]
discount = 0.6
for i in price_sheet:
    discount_usd = i*discount
    new_price = i-discount_usd     
    print(f'Starting price: ${i:.2f}, Discount amount: ${discount_usd:.2f}., New price: ${new_price:.2f}')

# exercise 65
for x in range(0,101,10):
    fahrenheit_temp = (x*9/5)+32
    print(f'Temperature in Celsius {x}C  or Fahrenheit {fahrenheit_temp:.0f}F')

# exercise 66 (did not pick up with the condition)
user_list = []
user_price = input('Enter your money: ')
while user_price !='':
    user_list.append(float(user_price))
    user_price = input('Enter your money: ')
print(f'User entered numbers: {user_list}. The sum of the digits entered by the user is ${sum(user_list)}')
cash_money = sum(user_list)*100 % 5
if cash_money < 5/2:
    cash_total = sum(user_list) - cash_money/100
else:
    cash_total = sum(user_list)+0.05 - cash_money/100

print(f'User entered numbers: {user_list}. The sum of the digits entered by the user is ${cash_total}')

# exercise 67
from math import sqrt
perimetr = 0

first_x = float(input('Enter X: '))
first_y = float(input('Enter Y: '))

prev_x = first_x
prev_y = first_y

line = input('Enter next x coordinat: ')

while line !='':
    x = float(line)
    y = float(input('Enter next coordinat Y: '))
    distance = sqrt((prev_x - x)**2 +(prev_y - y)**2)
    perimetr = perimetr + distance
    prev_x = x
    prev_y = y
    line = input('Enter next x coordinat: ')
distance = sqrt((first_x - x)**2 +(first_y - y)**2)
perimetr = perimetr + distance
print('Perimetr: ', perimetr)

# exercise 68
user_data = []
user_grade = input('Enter you letter grade:').upper()

dict_letter_number = {'A+': 4.0, 'A': 4.0, 'A-': 3.7, 'B+': 3.3, 'B': 3.0,
                    'B-': 2.7, 'C+': 2.3, 'C': 2.0, 'C-': 1.7, 'D+': 1.3,
                    'D': 1.0, 'F': 0,
                    }
while user_grade in dict_letter_number:
    user_data.append(dict_letter_number[user_grade])
    if user_grade in dict_letter_number:
        print(f'Entered value {user_grade}. You\'re grade is {dict_letter_number[user_grade]}')
    else:
        print(f'Entered value {user_grade}. Bro you made a mistake!')
    user_grade = input('Enter you letter grade:').upper()
sum_data = sum(user_data)/len(user_data)
print(sum_data)

# exercise 69
child_3 = 0.00
child_3_13 = 14.00
adult_13_65 = 23.00
pensioner = 18.00


age_visitors = []

age_visitor = input('Enter your age:')

while age_visitor !='':
    age = int(age_visitor)    
    
    if 0<=age<=3:             
        age_visitors.append(child_3)
        print(f'Your are entered age is {age}. Ticket price is {child_3}')   
    elif 3<age<=13:
        age_visitors.append(child_3_13)
        print(f'Your are entered age is {age}. Ticket price is {child_3_13}')    
    elif 13<age<=65:
        age_visitors.append(adult_13_65)
        print(f'Your are entered age is {age}. Ticket price is {adult_13_65}')
    elif 65<age:
        age_visitors.append(pensioner)
        print(f'Your are entered age is {age}. Ticket price is {pensioner}')    
    else:
        print('You entered the incorrect age of the visitor! Try again! ')
    age_visitor = input('Enter your age:')
print(f'Total amount - ${sum(age_visitors)} ')

# exercise 70
sum_bit = 0
len_total = []
user_bit = input('')
while user_bit !='' and len(len_total) < 8:    
    if user_bit == '1' or user_bit == '0':
        sum_bit += int(user_bit)
        len_total.append(user_bit)    
        user_bit = input('')
    else:
        print(f'You entered {user_bit} this is not "0" or "1". Try again please')
        user_bit = input('')
if int(len_total.count('1')) % 2 == 0:
    print('Parity bit is 0')
else:
    print('Parity bit is 1')
print(len_total)

# exercise 71
check = 0
CONST3 = 3
NUM4 = 4
start2 = 0
start3 = 1
start4 = 2 
while check < 15:
    check += 1
    start2 += 2
    start3 += 2
    start4 += 2 
    if check%2 != 0:
        iter = NUM4/((start2)*(start3)*(start4))
        CONST3 +=iter
    elif check%2 == 0:
        iter = -(NUM4/((start2)*(start3)*(start4)))
        CONST3 +=iter

print(CONST3)
    
#exercise 72
for i in range(1,101):
    if i % 3==0 and i % 5==0:
        print(f'Number {i} Fizz-Buzz')
    elif i % 3==0:
        print(f'Number {i} Fizz')
    elif i % 5==0:
        print(f'Number {i} Buzz')
    else:
        pass

# exercise 73 (35 strings)
user_phrase = input('Entered your phrase: ').lower()
user_encoding = int(input('Enter encoding variant'))
alphabet = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')
for x in user_phrase:
    if x in alphabet:        
        #print(f'Old values: {alphabet.index(x)}. New values {alphabet.index(x)+1}')
        print(alphabet[alphabet.index(x)+user_encoding], end='')

# exercise 74 (14 strings)

# exercise 75 (26 strings)
word = input('')
if word == word[::-1]:
    print('This word is palindrome!')
else:
    print('This word is not palindrome!')
#exercise 75 (26 strings) ver 2
word = list(input('').lower())
new_word = []
for x in word[::-1]:
    new_word.append(x)
if word == new_word:
    print('This word is palindrome!')
else:
    print('This word is not palindrome!')