import functions as fn

if __name__ == '__main__':

    while True:
        category = input('\nКатегорія:\n' +
                         '1. Допустимі нев\'язки для нівелювання різними класами\n'
                         '2. Горизонт приладу і висота проміжної точки\n'
                         '3. Нівелювання траси і колова крива\n'
                         '--->')

        if category == '1':
            task = input('Обчислити:\n' +
                         '1. Допустима нев\'язка для нівелювання IV класу\n' 
                         '2. Допустима нев\'язка для технічного нівелювання\n'
                         '-->')

            if task == '1':
                try:
                    length = input('Введіть відстань L в км -->')
                    length = fn.coma_replace(length)
                    fn.permissible_residual_leveling_4class(length)

                except ValueError:
                    print('ВВЕДИ ЧИСЛО!!!')

            elif task == '2':
                try:
                    length = input('Введіть відстань L в км -->')
                    length = fn.coma_replace(length)
                    fn.permissible_residual_technical_leveling(length)

                except ValueError:
                    print('ВВЕДИ ЧИСЛО!!!')

            else:
                print('ВВЕДИ ЧИСЛО!!!')

        elif category == '2':
            task = input('Обчислити:\n' +
                         '1. Висоти проміжної точки, маючи a, c, h\n'
                         '2. Горизонт приладу, маючи h задньої рейки та її відліки\n'
                         '-->')

            if task == '1':
                try:
                    h = input('Введіть h задньої точки -->')
                    a = input('Введіть a задньої точки -->')
                    c = input('Введіть c задньої точки -->')
                    h, a, c = fn.coma_replace(h), fn.coma_replace(a), fn.coma_replace(c)
                    fn.intermediate_point_height(h, a, c)

                except ValueError:
                    print('ВВЕДИ ЧИСЛО!!!')

            elif task == '2':
                try:
                    h = input('Введіть h задньої точки -->')
                    a = input('Введіть a задньої точки -->')
                    h, a = fn.coma_replace(h), fn.coma_replace(a)
                    fn.device_horizon(h, a)

                except ValueError:
                    print('ВВЕДИ ЧИСЛО!!!')

            else:
                print('ВВЕДИ ЧИСЛО!!!')

        elif category == '3':
            task = input('Обчислити:\n' +
                         '1. Проектну висоту H2, маючи ухил i, висоту H1 і відстань d\n'
                         '2. Ухил i, маючи висоти H1, H2 і відстань d\n'
                         '3. Тангенс колової кривої Т, маючи радіус R і бісектрису Б\n'
                         '4. Бісектрису Б, маючи радіус R і кут повороту\n'
                         '5. Колову криву К, маючи радіус R і кут повороту\n'
                         '6. Відстань від пікету до точки нульових робіт по x\n'
                         '7. Відстань від пікету до точки нулбових робіт по y\n'
                         '8. Тангенс Т, маючи колову криву К, домір Д, бісектрису Б\n'
                         '9. Криву К при тангенсі Т, домірі Д, бісектрисі Б\n'
                         '10. Кут повороту, маючи радіус R і тангенс\n'
                         '11. Криву К, маючи тангенс Т і бісектрису Б\n'
                         '12. Криву при радіусі R і кут повороту\n'
                         '13. Бісектрису, маючи тангенс Т і радіус R\n'
                         '14. Домір Д при радіус R і кут повороту\n'
                         '15. Криву К, маючи тангенс Т і домір Д\n'
                         '16. Тангенс Т при куті повороту і радіусі R\n'
                         '-->')

            if task == '1':
                try:
                    h1 = input('Введіть висоту 1-ої точки h1 -->')
                    i = input('Введіть ухил i -->')
                    d = input('Введіть відстань d -->')
                    h1, i, d = fn.coma_replace(h1), fn.coma_replace(i), fn.coma_replace(d)
                    fn.project_height2(h1, i, d)

                except ValueError:
                    print('ВВЕДИ ЧИСЛО!!!')

        else:
            print('ВВЕДИ ЧИСЛО!!!')
