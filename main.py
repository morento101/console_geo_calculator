import functions as fn

if __name__ == '__main__':

    while True:
        category = input('\nКатегорія:\n' +
                         '1. Допустимі нев\'язки для нівелювання різними класами\n' +
                         '2. Нівелювання траси\n'
                         '--->')

        if category == '1':
            task = input('Обчислити:\n' +
                         '1. Допустима нев\'язка для нівелювання IV класу\n' +
                         '2. Допустима нев\'язка для технічного нівелювання\n' +
                         '-->')

            if task == '1':
                try:
                    length = input('Введіть відстань L в км -->')
                    length = fn.coma_replace(length)
                    fn.permissible_residual_leveling_4class(length)

                except Exception:
                    print('ВВЕДИ ЧИСЛО!!!')

            elif task == '2':
                try:
                    length = input('Введіть відстань L в км -->')
                    length = fn.coma_replace(length)
                    fn.permissible_residual_technical_leveling(length)

                except Exception:
                    print('ВВЕДИ ЧИСЛО!!!')

            else:
                print('ВВЕДИ ЧИСЛО!!!')

        elif category == '2':
            task = input('Обчислити:\n' +
                         '1. Висоти проміжної точки, маючи a, c, h\n' +
                         '2. Горизонт приладу, маючи h задньої рейки та її відліки\n' +
                         '-->')

            if task == '1':
                try:
                    h = input('Введіть h задньої точки -->')
                    a = input('Введіть a задньої точки -->')
                    c = input('Введіть c задньої точки -->')
                    h, a, c = fn.coma_replace(h), fn.coma_replace(a), fn.coma_replace(c)
                    fn.intermediate_point_height(h, a, c)

                except Exception:
                    print('ВВЕДИ ЧИСЛО!!!')

            elif task == '2':
                try:
                    h = input('Введіть h задньої точки -->')
                    a = input('Введіть a задньої точки -->')
                    h, a = fn.coma_replace(h), fn.coma_replace(a)
                    fn.device_horizon(h, a)

                except Exception:
                    print('ВВЕДИ ЧИСЛО!!!')

            else:
                print('ВВЕДИ ЧИСЛО!!!')

        else:
            print('ВВЕДИ ЧИСЛО!!!')
