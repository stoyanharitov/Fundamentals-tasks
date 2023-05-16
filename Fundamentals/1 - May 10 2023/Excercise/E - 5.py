orders = int(input())
price = 0
total_price = 0

for i in range(orders):
    price_per_caps = float(input())
    days = int(input())
    caps_per_day = int(input())
    if price_per_caps < 0.01 or price_per_caps > 100:
        continue
    if days < 1 or days > 31:
        continue
    if caps_per_day < 1 or caps_per_day > 2000:
        continue
    price = price_per_caps*days*caps_per_day
    total_price += price
    print(f'The price for the coffee is: ${price:.2f}')

print(f'Total: ${total_price:.2f}')