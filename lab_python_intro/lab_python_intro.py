import sys
import math

def get_coef(index, prompt):

    try:
# Пробуем прочитать коэффициент из командной строки
        coef_str = sys.argv[index]
    except:
# Вводим с клавиатуры
        tester = False
        coef = 0.0
# проверка ввода корректности
        while (tester != True):
            print(prompt)
            coef_str = input()
            try:
                coef = float(coef_str)
                tester = True                
            except ValueError:
                tester = False
                print("Некорректный ввод\n")        
    return coef


def get_roots(a, b, c):
    result = []
    D = b*b - 4*a*c
    if D == 0.0:
        root = -b / (2.0*a) 
        if root > 0.0:
            x11=math.sqrt(root)
            x21=-math.sqrt(root)
            result.append(x11)
            result.append(x21)
        else:
            result.append('Нет корней')
            result.append('Нет корней')
    elif D > 0.0:
        sqD = math.sqrt(D)
        root1 = (-b + sqD) / (2.0*a)
        root2 = (-b - sqD) / (2.0*a)
        
        if root1>0 and root2>0:
            x1=math.sqrt(root1)
            x2=-math.sqrt(root1)
            x3=math.sqrt(root2)
            x4=-math.sqrt(root2)     
            result.append(x1)
            result.append(x2)
            result.append(x3)
            result.append(x4)
        elif root1 >0 and root2 < 0:
            x1=math.sqrt(root1)
            x2=-math.sqrt(root1)
            result.append(x1)
            result.append(x2)
            result.append('Нет корней')
            result.append('Нет корней')
        elif root1 <0 and root2 > 0:
            x3=math.sqrt(root2)
            x4=-math.sqrt(root2)
            result.append('Нет корней')
            result.append('Нет корней')
            result.append(x3)
            result.append(x4)
        else:
            result.append('Нет корней')
            result.append('Нет корней')
            result.append('Нет корней')
            result.append('Нет корней')
    return result

def main():
    '''
    Основная функция
    '''
    a = get_coef(1, 'Введите коэффициент А:')
    b = get_coef(2, 'Введите коэффициент B:')
    c = get_coef(3, 'Введите коэффициент C:')
    # Вычисление корней
    roots = get_roots(a,b,c)
    # Вывод корней
    len_roots = len(roots)
    if len_roots == 0:
        print('Нет корней')
    elif len_roots == 2:
        print('Один корень: x1 = {}; x2 = {}'.format(roots[0],roots[1]))
    elif len_roots == 4:
        print('Два корня: x1 = {}; x2 = {}; x3 = {}; x4 = {}'.format(roots[0], roots[1], roots[2], roots[3]))
    
# Если сценарий запущен из командной строки
if __name__ == "__main__":
    main()
