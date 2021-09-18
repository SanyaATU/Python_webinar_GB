spisok = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
new_spisok = []
for n in spisok:
    if n.replace("+", "").isdigit():
        if n.isdigit():
            new_spisok.append(f'"{int(n):02}"')
        else:
            new_spisok.append(f'"{n[0]}{int(n[1:]):02}"')
    else:
        new_spisok.append(n)
print(new_spisok)
print(" ".join(new_spisok))
