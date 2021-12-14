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