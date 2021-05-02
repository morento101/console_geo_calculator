import functions as fn

if __name__ == '__main__':

    while True:
        category = input('\nКатегорія:\n' +
                         '1. Допустимі нев\'язки для нівелювання різними класами\n'
                         '2. Горизонт приладу і висота проміжної точки\n'
                         '3. Нівелювання траси і колова крива\n'
                         '--->')

        if category == '1':
            task = input('\nОбчислити:\n' +
                         '1. Допустима нев\'язка для нівелювання IV класу\n' 
                         '2. Допустима нев\'язка для технічного нівелювання\n'
                         '-->')

            if task == '1':
                try:
                    length = input('\nВведіть відстань L в км:')
                    perm_res = fn.permissible_residual_leveling_4class(length)
                    print(f'Результат: {perm_res} мм')

                except ValueError:
                    print('ВВЕДИ ЧИСЛО!!!')

            elif task == '2':
                try:
                    length = input('\nВведіть відстань L в км:')
                    perm_res = fn.permissible_residual_technical_leveling(length)
                    print(f'Результат: {perm_res} мм')

                except ValueError:
                    print('ВВЕДИ ЧИСЛО!!!')

            else:
                print('ВВЕДИ ЧИСЛО!!!')

        elif category == '2':
            task = input('\nОбчислити:\n'
                         '1. Горизонт приладу, маючи h задньої рейки та її відліки\n'
                         '2. Висоти проміжної точки, маючи h, a, c\n'
                         '-->')

            if task == '1':
                try:
                    h = input('\nВведіть h задньої точки:')
                    a = input('Введіть a задньої точки:')
                    dev_horizon = fn.device_horizon(h, a)
                    print(f'Результат: {dev_horizon} м')

                except ValueError:
                    print('ВВЕДИ ЧИСЛО!!!')

            elif task == '2':
                try:
                    h = input('\nВведіть h задньої точки:')
                    a = input('Введіть відлік чорної шкали a задньої точки:')
                    c = input('Введіть відлік чорної шкали c проміжної точки:')
                    inter_point_h = fn.intermediate_point_height(h, a, c)
                    print(f'Результат: {inter_point_h} м')

                except ValueError:
                    print('ВВЕДИ ЧИСЛО!!!')

            else:
                print('ВВЕДИ ЧИСЛО!!!')

        elif category == '3':
            task = input('\nОбчислити:\n' +
                         '1. Проектну висоту H2, маючи ухил i, висоту H1 і відстань d\n'
                         '2. Ухил i, маючи висоти H1, H2 і відстань d\n'
                         '3. Тангенс колової кривої Т, маючи радіус R і бісектрису Б\n'
                         '4. Тангенс Т, маючи колову криву К, домір Д\n'
                         '5. Тангенс Т при куті повороту і радіусі R\n'
                         '6. Бісектрису Б, маючи радіус R і кут повороту\n'
                         '7. Бісектрису Б, маючи тангенс Т і радіус R\n'
                         '8. Відстань від пікету до точки нульових робіт по x\n'
                         '9. Відстань від пікету до точки нулбових робіт по y\n'
                         '10. Криву К, маючи радіус R і кут повороту\n'
                         '11. Криву К при тангенсі Т, домірі Д, бісектрисі Б\n'
                         '12. Кут повороту, маючи радіус R і тангенс\n'
                         '13. Криву К, маючи тангенс Т і бісектрису Б\n'
                         '14. Криву К при радіусі R і куті повороту\n'
                         '15. Домір Д при радіус R і кут повороту\n'
                         '16. Криву К, маючи тангенс Т і домір Д\n'
                         '-->')

            if task == '1':
                try:
                    h1 = input('\nВведіть висоту 1-ої точки h1:')
                    i = input('Введіть ухил i:')
                    d = input('Введіть відстань d:')
                    h2 = fn.project_height2(h1, i, d)
                    print(f'Результат: {h2} м')

                except ValueError:
                    print('ВВЕДИ ЧИСЛО!!!')

            elif task == '2':
                try:
                    h1 = input('\nВведіть висоту першої точи:')
                    h2 = input('Введіть висоту другої точки:')
                    d = input('Введіть відстань d:')
                    slope = fn.calc_slope(h1, h2, d)
                    print(f'Результат {slope} проміле')

                except ValueError:
                    print('ВВЕДИ ЧИСЛО!!!')

            elif task == '3':
                try:
                    r = input('\nВведіть радіус R:')
                    b = input('Введіть бісектрисц Б:')
                    tangent = fn.calc_tan_having_radius_bisector(r, b)
                    print(f'Результат {tangent} м')

                except ValueError:
                    print('ВВЕДИ ЧИСЛО!!!')

            elif task == '4':
                try:
                    m = input('\nВведіть домір Д:')
                    c = input('Введіть криву К:')
                    tangent = fn.calc_tan_having_curve_measure(m, c)
                    print(f'Результат {tangent} м')

                except ValueError:
                    print('ВВЕДИ ЧИСЛО!!!')

            elif task == '5':
                try:
                    angle = input('\nВведіть кут повороту через пробіл\n' 
                                  '(180 30 20 = 180°30\'20\'\'):')
                    radius = input('Введіть радіус R:')
                    tangent = fn.calc_tan_having_angle_radius(angle, radius)
                    print(f'Результат {tangent} м')

                except ValueError:
                    print('ВВЕДИ ЧИСЛО!!!')

            elif task == '6':
                try:
                    angle = input('\nВведіть кут повороту через пробіл\n'
                                  '(180 30 20 = 180°30\'20\'\'):')
                    radius = input('Введіть радіус R:')
                    bisector = fn.calc_bisector_having_radius_angle(radius, angle)
                    print(f'Результат {bisector} м')

                except ValueError:
                    print('ВВЕДИ ЧИСЛО!!!')

            elif task == '7':
                try:
                    tangent = input('\nВведіть тангенс Т:')
                    radius = input('Введіть радіус R:')
                    bisector = fn.calc_bisector_having_tangent_radius(tangent, radius)
                    print(f'Результат {bisector} м')

                except ValueError:
                    print('ВВЕДИ ЧИСЛО!!!')

            elif task == '8':
                try:
                    h1 = input('\nВведіть першу робочу відмітку:')
                    h2 = input('Введіть другу робочу відмітку:')
                    d = input('Введіть відстань d:')
                    x = fn.distance_from_0work_by_x(h1, h2, d)
                    print(f'Результат {x} м')

                except ValueError:
                    print('ВВЕДИ ЧИСЛО!!!')

            elif task == '9':
                try:
                    h1 = input('\nВведіть першу робочу відмітку:')
                    h2 = input('Введіть другу робочу відмітку:')
                    d = input('Введіть відстань d:')
                    y = fn.distance_from_0work_by_y(h1, h2, d)
                    print(f'Результат {y} м')

                except ValueError:
                    print('ВВЕДИ ЧИСЛО!!!')

            else:
                print('ВВЕДИ ЧИСЛО!!!')

        else:
            print('ВВЕДИ ЧИСЛО!!!')
