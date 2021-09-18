from random import uniform
prices = [uniform(1, 101) for i in range(101)]

for i in prices:
    rub, kop = int(i // 1), int(f"{i % 1:.02f}"[2:])
    print(f"{rub} руб {kop:02d} коп,", end=" ")

print(f"prices: {prices}")
prices.sort()
print(f"prices ^: {prices}")
n_list = sorted(prices, reverse=True)
print(f"prices v: {n_list}\n{n_list[:5][::-1]}")
