import functions as fn


while True:
    category = input('\nКатегорія:\n' +
                     '1. Допустимі нев\'язки для нівелювання різними класами\n' +
                     '2. Нівелювання траст\n'
                     '--->')

    if category == '1':
        task = input('Обчислити:\n' +
                     '1. Допустима нев\'язка для нівелювання IV класу\n' +
                     '2. Допустима нев\'язка для технічного нівелювання\n' +
                     '-->')

        if task == '1':
            len = float(input('Введіть відстань L в км -->'))
            fn.permissible_residual_leveling_4class(len)

        if task == '2':
            len = float(input('Введіть відстань L в км -->'))
            fn.permissible_residual_technical_leveling(len)

    if category == '2':
        task = input('Обчислити:\n' +
                     '1. Висоти проміжної точки, маючи a, c, h\n' +
                     '2. Горизонт приладу, маючи h задньої рейки та її відліки\n' +
                     '-->')

        if task == '1':
            h = float(input('Введіть h задньої точки -->'))
            a = float(input('Введіть с задньої точки -->'))
            fn.intermediate_point_height(h, a)


