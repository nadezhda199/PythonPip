def compl_1(items): # первое комплексное число
    x1 = float(items[0])  # вешественная часть первого числа
    x2 = float(items[1])  # мнимая часть первого числа
    x = complex(x1, x2)
    return x

def compl_2(items): # второе комплексное число
    y1 = float(items[2])  # вешественная часть второго числа
    y2 = float(items[3])  # мнимая часть второго числа
    y = complex(y1, y2)
    return y