for i in list(range(1, 101)):
    if i % 10 == 1:
        if i // 10 == 1:
            print(f"{i} процентов")
        else:
            print(f"{i} процент")
        continue
    if i % 10 == 2 or i % 10 == 3 or i % 10 == 4:
        if i // 10 == 1:
            print(f"{i} процентов")
        else:
            print(f"{i} процента")
        continue
    if i % 10 == 5 or i % 10 == 6 or i % 10 == 7 or i % 10 == 8 or i % 10 == 9 or i % 10 == 0:
        print(f"{i} процентов")
        continue
    i += 1
