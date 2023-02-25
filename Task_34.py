def fy(words):
    return sum(1 for i in words if i in "аеёиоуыэюя")
    
    
text = "Хорошо-живет-на-свете-Винни-Пух! Оттого-поет-он-эти-Песни-вслух!"

st = text.lower().split()
t = fy(st[0])

if all([fy(i) == t for i in st]):
    print("Парам пам-пам")
else:
    print("Пам парам")