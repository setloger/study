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