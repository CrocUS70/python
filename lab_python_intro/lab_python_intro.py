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
        if root >= 0.0:
            x11=math.sqrt(root)
            x21=-1 *math.sqrt(root)
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
            x2= -1 * math.sqrt(root1)
            x3=math.sqrt(root2)
            x4= -1 *math.sqrt(root2)     
            result.append(x1)
            result.append(x2)
            result.append(x3)
            result.append(x4)
        elif root1 >0 and root2 < 0:
            x1=math.sqrt(root1)
            x2= -1 *math.sqrt(root1)
            result.append(x1)
            result.append(x2)
            result.append('Нет корней')
            result.append('Нет корней')
        elif root1 <0 and root2 > 0:
            x3=math.sqrt(root2)
            x4=-1 *math.sqrt(root2)
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

def lin(b, c):
    result = []
    root = 0.0
    root = -1 * c / b
    if root > 0:
    	root1 = math.sqrt(root)
    	root2 = -1 *math.sqrt(root)
    	result.append(root1)
    	result.append(root2)
    elif root == 0:
    	result.append(root)
    return result



def main():
    
    a = get_coef(1, 'Введите коэффициент А:')
    b = get_coef(2, 'Введите коэффициент B:')
    c = get_coef(3, 'Введите коэффициент C:')
    roots =[]
    if a == 0.0:
    	if c ==0.0:
    	    if b ==0.0:
    	    	roots = [1,1,1,1,1]
    	    else:
    	    	roots = [1]
    	elif b ==0.0:
    	    roots = []
    	else:
    	    roots = lin(b, c)
    # Вычисление корней
    
    else:
        roots = get_roots(a,b,c)
    # Вывод корней
    len_roots = len(roots)
    if len_roots == 0:
        print('Нет корней')
    elif len_roots == 1:
        print('x = 0')
    elif len_roots == 2:
        print('Один корень : x1 = {}; x2 = {}'.format(roots[0],roots[1]))
    elif len_roots == 4:
        print('Два корня : x1 = {}; x2 = {}; x3 = {}; x4 = {}'.format(roots[0], roots[1], roots[2], roots[3]))
    elif len_roots == 5:
        print('Любое число - x')
# Если сценарий запущен из командной строки
if __name__ == "__main__":
    main()
