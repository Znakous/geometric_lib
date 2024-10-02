def area(a, h): 
    '''Возвращает площадь треугольника с указанными стороной a и высотой h
        Параметры:
            a (int): длина одной из сторон треугольника
            h (int): длина перпендикулярной ей высоты
        Возвращаемое значение:
            area (int): площадь искомого треугольника
    '''
    return a * h / 2 

def perimeter(a, b, c): 
    '''Возвращает периметр треугольника с указанными сторонами a, b и c
        Параметры:
            a (int): длина первой стороны треугольника
            b (int): длина второй стороны треугольника
            c (int): длина третьей стороны треугольника
        Возвращаемое значение:
            perimeter (int): периметр искомого треугольника
    '''
    return a + b + c 
