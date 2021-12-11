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