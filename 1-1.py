duration = int(input('duration = '))
d = int(duration // 86400)
h = int(duration // 3600)
m = int((duration % 3600) / 60)
s = int(duration % 60)
if duration < 60:
    print(f"{duration} сек")
elif duration >= 60:
    if duration < 3600:
        print(f"{m} мин {s} сек")
    elif duration < 86400:
        print(f"{h} час {m} мин {s} сек")
    else:
        h = int((duration % 86400) / 3600)
        print(f"{d} дн {h} час {m} мин {s} сек")