customer = input('Enter customer name: ')
product = input('Enter product name: ')
price = input('Enter price per unit (KZT): ')
quantity = input('Enter quantity: ')


subtotal = int(price) * int(quantity)
discount = subtotal/10 if subtotal > 5000 else 0
total = subtotal - discount

print('=' * 30)
print('\t\t SHOP RECEIPT')
print('=' * 30)
print(f'Customer : {customer}')
print(f'Product : {product}')
print(f'Price : {price} KZT')
print(f'Quantity : {quantity}')
print('-' * 30)
print(f'Subtotal : {subtotal} KZT')
print(f'Discount : {discount} KZT')
print(f'Total : {total} KZT')
print('=' * 30)
print(f'Discount applied : {subtotal>5000}')
print(f'Paid more than 3000 : {total>3000}')