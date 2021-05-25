import functions as fn

if __name__ == '__main__':

    while True:
        category = input('\nКатегорія:\n' +
                         '1. Допустимі нев\'язки для нівелювання різними класами\n'
                         '2. Горизонт приладу і висота проміжної точки\n'
                         '3. Нівелювання траси і колова крива\n'
                         '4. Барометричне нівелювання\n'
                         '5. Тахеометричне знімання\n'
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
                         '11. Криву К при тангенсі Т, домірі Д\n'
                         '12. Кут повороту, маючи радіус R і тангенс\n'
                         '13. Домір Д при радіус R і кут повороту\n'
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

            elif task == '10':
                try:
                    radius = input('\nВведіть радіус R:')
                    angle = input('Введіть кут повороту через пробіл\n'
                                  '(180 30 20 = 180°30\'20\'\'):')
                    curve = fn.curve_having_radius_angle(radius, angle)
                    print(f'Результат {curve} м')

                except ValueError:
                    print('ВВЕДИ ЧИСЛО!!!')

            elif task == '11':
                try:
                    tangent = input('\nВведіть тангенс Т:')
                    measure = input('Введіть домір Д:')
                    curve = fn.curve_having_tangent_measure(tangent, measure)
                    print(f'Результат {curve} м')

                except ValueError:
                    print('ВВЕДИ ЧИСЛО!!!')

            elif task == '12':
                try:
                    radius = input('\nВведіть радіус R:')
                    tangent = input('Введіть тангенс Т:')
                    angle = fn.angle_having_radius_tangent(radius, tangent) / fn.ONE_RAD
                    degrees, minutes, seconds = fn.convert_decimal_degrees_to_degrees(angle)
                    print(f'Результат {degrees}°{minutes}\'{seconds}\'\'')

                except ValueError:
                    print('ВВЕДИ ЧИСЛО!!!')

            elif task == '13':

                radius = input('\nВведіть радіус R:')
                angle = input('Введіть кут повороту через пробіл\n'
                              '(180 30 20 = 180°30\'20\'\'):')
                measure = fn.calc_measure_having_radius_angle(radius, angle)
                print(f'Результат {measure} м')

            else:
                print('ВВЕДИ ЧИСЛО!!!')

        elif category == '4':
            task = input('\nОбчислити:\n'
                         '\n1. Тиск  на певному  поверсі, знаючи висоту поверха, бар. ступ. \n'
                         '2. Висоту будівлі, знаючи тиск у двох точках\n'
                         '-->')

            if task == '1':
                try:
                    known_floor = input('\nВведіть номер відомого поверху:')
                    pressure_on_known_floor = input('Введіть тиск на відомому поверсі:')
                    seek_floor = input('Введіть номер шуканого поверху:')
                    floor_height = input('Введіть висоту одного поверху:')
                    barometric_degree = input('Введіть барометричну ступінь (якщо не вказано, то введи 11):')
                    pressure_on_seek_floor = fn.calc_pressure_on_cert_floor(known_floor, pressure_on_known_floor,
                                                                            seek_floor, floor_height, barometric_degree)
                    print(f'Результат {pressure_on_seek_floor} мм рт. ст.')

                except ValueError:
                    print('ВВЕДИ ЧИСЛО!!!')

            elif task == '2':
                try:
                    pressure_floor1 = input('\nВведіть тиск на першому поверсу:')
                    pressure_floor2 = input('Введіть тиск на другому поверсі:')
                    barometric_degree = input('Введіть барометричну ступінь (якщо не вказано, то введи 11):')
                    height_difference = fn.calc_height_of_building(pressure_floor1, pressure_floor2, barometric_degree)
                    print(f'Результат {height_difference} м')

                except ValueError:
                    print('ВВЕДИ ЧИСЛО!!!')

        elif category == '5':
            task = input('\nОбчислити:\n'
                         '1. Допустима висотна нев\'язка, знаючи периметр\n'
                         '2. Висота пікету, маючи висоту точки стояння, перевищення, l, i\n'
                         '3. Місце нуля\n'
                         '4. Кут нахилу при МО і КП\n'
                         '5. Кут нахилу при МО і КЛ\n'
                         '6. Кут нахилу при КЛ і КП\n'
                         '7. Перевищення h, маючи віддяль D, верт. кут v, висоту приладу i, вис. наведення l\n'
                         '8. Абсолютну лінійну нев\'язку, маючи координати поч. і кін. точок X, Y\n'
                         '9. Горизонтальну проекцію d, маючи відстань D виміряну мірною стрічкою і кут нахилу v\n'
                         '10. Горизонтальну проекцію d, маючи відстань D виміряну віддалеміром і кут нахилу v\n'
                         '11. Висотну нев\'язку, маючи висоту початкової та кінцевої точок Hпоч і Hкін та практичну '
                         'суму первищень Σhсер\n'
                         '12. Горизонтальну проекцію, маючи координати початкової та кінцевої точок\n'
                         '-->')

            if task == '1':
                try:
                    perimeter = input('\nВведіть периметр:')
                    n = input('Введіть к-сть перевищень:')
                    perm_height_residual = fn.permissible_height_residual(perimeter, n)
                    print(f'Результат +-{perm_height_residual} м')

                except ValueError:
                    print('ВВЕДИ ЧИСЛО!!!')

            elif task == '2':
                try:
                    h1 = input('\nВведіть висоту точки стояння:')
                    h = input('Введіть перевищення h:')
                    i = input('Введіть висоту приладу i:')
                    l = input('Введуть висоту наведення l:')
                    h2 = fn.h2_having_h1_l_i(h1, h, i, l)
                    print(f'Результат {h2} м')

                except ValueError:
                    print('ВВЕДИ ЧИСЛО!!!')

            elif task == '3':
                try:
                    kp = input('\nВведіть відлік КП через пробіл:'
                               '(180 30 20 = 180°30\'20\'\'):')
                    kl = input('Введіть відлік КЛ через пробіл'
                               '(180 30 20 = 180°30\'20\'\'):')
                    z_spot_degrees, z_spot_minutes, z_spot_seconds = fn.calc_zero_spot(kp, kl)
                    print(f'Результат {z_spot_degrees}°{z_spot_minutes}\'{z_spot_seconds}\'\'')

                except ValueError:
                    print('ВВЕДИ ЧИСЛО!!!')

            elif task == '4':
                try:
                    zero_spot = input('\nВведіть відлік МО через пробіл\n'
                                      '(180 30 20 = 180°30\'20\'\'):')
                    kp = input('Введіть відлік КП через пробіл\n'
                               '(180 30 20 = 180°30\'20\'\'):')
                    degrees, minutes, seconds = fn.calc_angle_having_mo_kp(zero_spot, kp)
                    print(f'Результат {degrees}°{minutes}\'{seconds}\'\'')

                except ValueError:
                    print('ВВЕДИ ЧИСЛО!!!')

            elif task == '5':
                try:
                    zero_spot = input('\nВведіть відлік МО через пробіл\n'
                                      '(180 30 20 = 180°30\'20\'\'):')
                    kl = input('Введіть відлік КЛ через пробіл\n'
                               '(180 30 20 = 180°30\'20\'\'):')
                    degrees, minutes, seconds = fn.calc_angle_having_mo_kp(zero_spot, kl)
                    print(f'Результат {degrees}°{minutes}\'{seconds}\'\'')

                except ValueError:
                    print('ВВЕДИ ЧИСЛО!!!')

            elif task == '6':
                try:
                    kl = input('\nВведіть відлік КЛ через пробіл\n'
                               '(180 30 20 = 180°30\'20\'\'):')
                    kp = input('Введіть відлік КП через пробіл\n'
                               '(180 30 20 = 180°30\'20\'\'):')
                    degrees, minutes, seconds = fn.angle_having_kl_kp(kl, kp)
                    print(f'Результат {degrees}°{minutes}\'{seconds}\'\'')

                except ValueError:
                    print('ВВЕДИ ЧИСЛО!!!')

            elif task == '7':
                try:
                    d = input('\nВведіть виміряну віддаль D:')
                    v = input('Введіть верт. кут v через пробіл\n'
                              '(180 30 20 = 180°30\'20\'\'):')
                    i = input('Введіть висоту приладу i:')
                    l = input('Введіть висоту наведення l\n'
                              '(Якщо не вказано  то дорівнює i):')
                    h = fn.h_having_d_v_i_l(d, v, i, l)
                    print(f'Результат {round(h, 2)} м')

                except ValueError:
                    print('ВВЕДИ ЧИСЛО!!!')

            elif task == '8':
                try:
                    x1 = input('\nВведіть Х початкової точки:')
                    y1 = input('Введіть Y початкової точки:')
                    xn = input('Введіть Х кінцевої точки:')
                    yn = input('Введіть Y кінцевої точки:')
                    practice_x = input('Введіть практичну суму Х:')
                    practice_y = input('Введіть практичну суму Y:')
                    abs_lin_residual = fn.absolute_lineal_residual_having_coords(x1, y1, xn, yn, practice_x, practice_y)
                    print(f'Результат {round(abs_lin_residual, 2)} м')

                except ValueError:
                    print('ВВЕДИ ЧИСЛО!!!')

            elif task == '9':
                try:
                    d = input('\nВведіть відстань D:')
                    v = input('Введіть кут нахилу v через пробіл\n'
                              '(180 30 20 = 180°30\'20\'\'):')
                    horizontal_projection = fn.horizontal_projection_string(d, v)
                    print(f'Результат {round(horizontal_projection, 2)} м')

                except ValueError:
                    print('ВВЕДИ ЧИСЛО!!!')

            elif task == '10':
                try:
                    d = input('\nВведіть відстань D:')
                    v = input('Введіть кут нахилу v через пробіл\n'
                              '(180 30 20 = 180°30\'20\'\'):')
                    horizontal_projection = fn.horizontal_projection_rangefinder(d, v)
                    print(f'Результат {round(horizontal_projection, 2)} м')

                except ValueError:
                    print('ВВЕДИ ЧИСЛО!!!')

            elif task == '11':
                try:
                    hst = input('\nВведіть висоту початкової точки:')
                    hfn = input('Введіть висоту кінцевої точки:')
                    pr_sum_excess = input('Введіть практичну суму всіх перевищень:')
                    height_residual = fn.height_residual(hst, hfn, pr_sum_excess)
                    print(f'Результат {round(height_residual, 2)} м')

                except ValueError:
                    print('ВВЕДИ ЧИСЛО!!!')

            elif task == '12':
                try:
                    x1 = input('\nВведіть Х початкової точки:')
                    y1 = input('Введіть Y початкової точки:')
                    xn = input('Введіть Х кінцевої точки:')
                    yn = input('Введіть Y кінцевої точки:')
                    horizontal_projection = fn.hor_proj_having_coords(x1, y1, xn, yn)
                    print(f'Результат {round(horizontal_projection, 2)} м')

                except ValueError:
                    print('ВВЕДИ ЧИСЛО!!!')

            elif task == '13':
                x1 = input('\nВведіть Х початкової точки:')
                y1 = input('Введіть Y початкової точки:')
                xn = input('Введіть Х кінцевої точки:')
                yn = input('Введіть Y кінцевої точки:')
                angle_degrees, angle_minutes, angle_seconds = fn.directory_angle(x1, y1, xn, yn)
                print(f'Результат {angle_degrees}°{angle_minutes}\'{angle_seconds}\'\'')

        else:
            print('ВВЕДИ ЧИСЛО!!!')  #TODO: fix this
