from math import sqrt
from fractions import Fraction as Frc
from decimal import Decimal as Dec

def discriminant(a, b, c, func=Dec, full_output=False):      # Пошук коренів через дискримінант
    a, b, c = map(func, (a, b, c))
    output = {}     # Вихідний словник

    D = b**2 - 4*a*c
    output['discr'] = D

    if D > 0:   # Перевірка дискримінанту
        Dsqrt = func(str(sqrt(D)))
        output['Dsqrt'] = Dsqrt

        x1 = (-b + Dsqrt) / (2*a)
        x2 = (-b - Dsqrt) / (2*a)

        output['Xs'] = tuple([x1, x2])  # Збереження результатів в кортежі під ключем 'Xs'
    elif D == 0:
        output['Dsqrt'] = func('0')

        x = -b / (2*a)

        output['Xs'] = tuple([x])
    else:
        output['Dsqrt'] = None
        output['Xs'] = tuple()

    return output if full_output else output['Xs']

def print_res(res, var='x'):    # Виведення результатів у консоль
    print('\nD =', res['discr'])
    print('√D =', str(res['Dsqrt']))

    if len(res['Xs']) == 2:
        print(f'{var}1 =', str(res['Xs'][0]).strip('.0'))
        print(f'{var}2 =', str(res['Xs'][1]).strip('.0'))
    elif len(res['Xs']) == 1:
        print('x =', str(res['Xs'][0]).strip('.0'))
    else:
        print('Немає коренів')

def to_multipliers(a, xs, var='x'):     # Функція розкладання на множники
    if a == '-1':     # Перший коефіцієнт
        output = '-'
    elif a == '1':
        output = ''
    else:
        output = str(a)
        
    for x in xs:    # Перші та другі дужки в залежності від коренів рівняння
        if x>0:
            output = output + f'({var} - {str(x).strip(".0")})'
        elif x<0:
            output = output + f'({var} + {str(abs(x)).strip(".0")})'
        else:
            output = output + var
    
    if len(xs) == 1:    # Якщо D = 0 піднести єдину дужку до квадрату
        output = output + '^2'
    
    return output

if __name__ == '__main__':
    print('''Ввід:
            a b c [змінна] [-f (для звичайних дробів)]
          
            [] - опціонально
          ''')
    while True:
        try:
            variable = 'x'
            frac = Dec
            a, b, c, *params = input(': ').split()     # Запит коефіцієнтів та змінної

            match params:
                case [var, '-f', *_]:
                    variable = var
                    frac = Frc
                case ['-f', *_]:
                    frac = Frc
                case [var, *_]:
                    variable = var
            
            if '/' in a + b + c:
                frac = Frc

            ans = discriminant(a, b, c, frac, full_output=True)
            print_res(ans, var=variable)

            if ans['Xs']:
                print('\n' + to_multipliers(a, ans['Xs'], var=variable))    # Виведення виразу, розкладеного на множники

        except KeyboardInterrupt:
            raise SystemExit()
        except Exception as error:
            print(error)