budget = float(input())
price_per_kilo_flour = float(input())
egg_count = 0
bread_count = 0

price_egg = price_per_kilo_flour * 0.75
price_milk = (price_per_kilo_flour * 1.25) / 4

price_per_bread = price_egg + price_per_kilo_flour + price_milk
total_price = 0

while True:
    bread_count += 1
    egg_count += 3
    total_price += price_per_bread
    if total_price > budget:
        print(f'You made {bread_count} loaves of Easter bread! Now you have {egg_count} eggs and {budget - total_price:2f}BGN left.')
        break
    if bread_count % 3 == 0:
        egg_count -= 2
print(price_milk)
print(price)