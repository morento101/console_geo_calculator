import math


ONE_RAD = 0.01745329252


def coma_replace(s):
    s = str(s)
    if ',' in s:
        s = s.replace(',', '.')
    if '−' in s:
        s = s.replace('−', '')
        s = 0 - float(s)
    return float(s)


def readout_convert_to_metres(readout):
    if len(readout) == 4:
        readout = readout[0] + '.' + readout[1:]
    else:
        readout = ''
    return float(readout)


def calc_asec(angle):
    return math.acos(1 / angle)


def calc_sec(angle):
    return 1 / math.cos(angle)


def convert_grad_min_secs_to_decimal(string):
    string = string.split(' ')

    if len(string) == 3:
        degrees, minutes, seconds = string[0], string[1], string[2]
        degrees, minutes, seconds = coma_replace(degrees), coma_replace(minutes), coma_replace(seconds)

        if float(degrees) > 0:
            decimal_degrees = (float(degrees) + (float(minutes) / 60) + (float(seconds) / 3600))
            return decimal_degrees

        elif float(degrees) < 0:
            decimal_degrees = (float(degrees) - (float(minutes) / 60) - (float(seconds) / 3600))
            return decimal_degrees

        elif str(degrees) == '0.0':
            decimal_degrees = 0 + (float(minutes) / 60) + (float(seconds) / 3600)
            return decimal_degrees

        elif str(degrees) == '-0.0':
            decimal_degrees = 0 - (float(minutes) / 60) - (float(seconds) / 3600)
            return decimal_degrees

    elif len(string) == 2:
        degrees, minutes = string[0], string[1]
        degrees, minutes = coma_replace(degrees), coma_replace(minutes)
        if float(degrees) > 0:
            decimal_degrees = (float(degrees) + (float(minutes) / 60))
            return decimal_degrees

        elif float(degrees) < 0:
            decimal_degrees = (float(degrees) - (float(minutes) / 60))
            return decimal_degrees

        elif str(degrees) == '0.0':
            decimal_degrees = 0 + (float(minutes) / 60)
            return decimal_degrees

        elif str(degrees) == '-0.0':
            decimal_degrees = 0 - (float(minutes) / 60)
            return decimal_degrees

    elif len(string) == 1:
        degrees = string[0]
        degrees = coma_replace(degrees)
        decimal_degrees = float(degrees)
        return decimal_degrees

    else:
        print('НЕПРАВИЛЬНИЙ ФОРМАТ!!!')


def convert_decimal_deg_to_rad(angle):
    rad = (angle * math.pi) / 180
    return rad


def convert_decimal_degrees_to_degrees(angle):
    if angle < 0:
        if round(angle) == 0:
            degrees = int(angle)
            minutes = int((angle - degrees) * 60)
            seconds = round((angle - degrees - (minutes / 60)) * 3600)
            return '-0', abs(minutes), abs(seconds)
        else:
            degrees = int(angle)
            minutes = int((angle - degrees) * 60)
            seconds = round((angle - degrees - (minutes / 60)) * 3600)
            return degrees, abs(minutes), abs(seconds)

    elif angle > 0:
        degrees = int(angle)
        minutes = int((angle - degrees) * 60)
        seconds = round((angle - degrees - (minutes / 60)) * 3600)
        return degrees, minutes, seconds

    elif angle == 0:
        degrees, minutes, seconds = 0, 0, 0
        return degrees, minutes, seconds


def convert_rad_to_decimal(angle):
    angle = angle * (180 / math.pi)
    return angle


def permissible_residual_leveling_4class(length):
    length = coma_replace(length)
    perm_res = 20 * math.sqrt(length)
    perm_res = math.ceil(perm_res)
    print(f'Допустима нев\'язка = 20 * корінь_квадратний({length}) = {round(perm_res, 2)}')
    return perm_res


def permissible_residual_technical_leveling(length):
    length = coma_replace(length)
    perm_res = 50 * math.sqrt(length)
    perm_res = math.ceil(perm_res)
    print(f'Допустима нев\'язка = 50 * корінь_квадратний({length}) = {round(perm_res, 2)}')
    return perm_res


def device_horizon(h, a):
    a = readout_convert_to_metres(a)
    h, a = coma_replace(h), coma_replace(a)
    dev_horizon = h + a
    print(f'ГП = {h} + {a} = {round(dev_horizon, 2)}')
    return round(dev_horizon, 3)


def intermediate_point_height(h, a, c):
    a, c = readout_convert_to_metres(a), readout_convert_to_metres(c)
    h, a, c = coma_replace(h), coma_replace(a), coma_replace(c)
    dev_horizon = h + a
    inter_point_h = dev_horizon - c
    print(f'ГП = {h} + {a} = {dev_horizon}')
    print(f'Проміжна = {dev_horizon} - {c} = {round(inter_point_h, 2)}')
    return round(inter_point_h, 3)


def project_height2(h1, i, d):
    h1, i, d = coma_replace(h1), coma_replace(i), coma_replace(d)
    h2 = (i * d) + h1
    print(f'Проектна висота 2 = {i} * {d} + {h1} = {round(h2, 2)}')
    return round(h2, 2)


def calc_slope(h1, h2, d):
    h1, h2, d = coma_replace(h1), coma_replace(h2), coma_replace(d)
    slope1 = ((h2 - h1) / d)
    slope2 = ((h2 - h1) / d) * 1000
    print(f'Ухил = {h2} - {h1} / {d} = {round(slope1)}')
    return round(slope1, 3), round(slope2)


def calc_tan_having_radius_bisector(r, b):
    r, b = coma_replace(r), coma_replace(b)
    angle = 2 * calc_asec((b / r) + 1)
    tangent = r * math.tan(angle / 2)
    degrees, minutes, seconds = convert_decimal_degrees_to_degrees(angle)
    print(f'Кут = 2 * asec({b} / {r} + 1) = {degrees}°{minutes}\'{seconds}\'\'')
    print(f'Т = {r} * tan({degrees}°{minutes}\'{seconds}\'\' / 2) = {round(tangent, 2)}')
    return round(tangent, 2)


def calc_tan_having_curve_measure(c, m):
    c, m = coma_replace(c), coma_replace(m)
    tangent = (m + c) / 2
    print(f'Т = ({m} + {c}) / 2 = {round(tangent, 2)}')
    return round(tangent, 2)


def calc_tan_having_angle_radius(angle, radius):
    angle, radius = convert_grad_min_secs_to_decimal(angle), coma_replace(radius)
    angle = convert_decimal_deg_to_rad(angle)
    tangent = radius * math.tan(angle / 2)
    degrees, minutes, seconds = convert_decimal_degrees_to_degrees(angle)
    print(f'Т = {radius} * tan({degrees}°{minutes}\'{seconds}\'\' / 2) = {round(tangent, 2)}')
    return round(tangent, 2)


def calc_bisector_having_radius_angle(radius, angle):
    angle, radius = convert_grad_min_secs_to_decimal(angle), coma_replace(radius)
    angle = convert_decimal_deg_to_rad(angle)
    bisector = radius * (calc_sec(angle / 2) - 1)
    degrees, minutes, seconds = convert_decimal_degrees_to_degrees(angle)
    print(f'Б = {radius} * sec({degrees}°{minutes}\'{seconds}\'\' / 2) - 1 = {round(bisector, 2)}')
    return round(bisector, 2)


def angle_having_radius_tangent(radius, tangent):
    radius, tangent = coma_replace(radius), coma_replace(tangent)
    angle = 2 * math.atan(tangent / radius) / ONE_RAD
    degrees, minutes, seconds = convert_decimal_degrees_to_degrees(angle)
    print(f'Кут = 2 * tan({tangent} / {radius}) = {degrees}°{minutes}\'{seconds}\'\'')
    return angle


def calc_bisector_having_tangent_radius(tangent, radius):
    tangent, radius = coma_replace(tangent), coma_replace(radius)
    angle = 2 * math.atan(tangent / radius)
    bisector = radius * (calc_sec(angle / 2) - 1)
    degrees, minutes, seconds = convert_decimal_degrees_to_degrees(angle)
    print(f'Кут = 2 * tan({tangent} / {radius} = {degrees}°{minutes}\'{seconds}\'\'')
    print(f'Б = {radius} * sec({degrees}°{minutes}\'{seconds}\'\' / 2) - 1 = {round(bisector, 2)}')
    return round(bisector, 2)


def distance_from_0work_by_x(h1, h2, d):
    h1, h2, d = coma_replace(h1), coma_replace(h2), coma_replace(d)
    x = (h1 * d) / (h1 + h2)
    print(f'Відстань по x = ({h1} * {d}) / ({h1} + {h2}) = {round(x, 2)}')
    return round(x, 2)


def distance_from_0work_by_y(h1, h2, d):
    h1, h2, d = coma_replace(h1), coma_replace(h2), coma_replace(d)
    y = (h2 * d) / (h1 + h2)
    print(f'Відстань по y = ({h2} * {d}) / ({h1} + {h2}) = {round(y, 2)}')
    return round(y, 2)


def curve_having_radius_angle(radius, angle):
    radius, angle = coma_replace(radius), convert_grad_min_secs_to_decimal(angle)
    angle = convert_decimal_deg_to_rad(angle)
    curve = radius * ((math.pi * angle) / (180 * ONE_RAD))
    degrees, minutes, seconds = convert_decimal_degrees_to_degrees(angle)
    print(f'К = {radius} * (pi * {degrees}°{minutes}\'{seconds}\'\') / 180° = {round(curve, 2)}')
    return round(curve, 2)


def curve_having_tangent_measure(tangent, measure):
    tangent, measure = coma_replace(tangent), coma_replace(measure)
    curve = 2 * tangent - measure
    print(f'К = 2 * {tangent} - {measure} = {round(curve, 2)}')
    return round(curve, 2)


def calc_measure_having_radius_angle(radius, angle):
    radius, angle = coma_replace(radius), convert_grad_min_secs_to_decimal(angle)
    angle = convert_decimal_deg_to_rad(angle)
    measure = radius * ((2 * math.tan(angle / 2)) - ((math.pi * angle) / (180 * ONE_RAD)))
    degrees, minutes, seconds = convert_decimal_degrees_to_degrees(angle)
    print(f'Д = {radius} * (2 * tan({degrees}°{minutes}\'{seconds}\'\' / 2) - (pi * {degrees}°{minutes}\'{seconds}\'\') / 180 = {round(measure, 2)}')
    return round(measure, 2)


def calc_pressure_on_cert_floor(known_floor, pressure_on_known_floor, seek_floor, floor_height, barometric_degree=11):
    pressure_on_seek_floor = 0

    pressure_on_known_floor, floor_height, barometric_degree = coma_replace(pressure_on_known_floor), coma_replace(
        floor_height), coma_replace(barometric_degree)

    known_floor, seek_floor = float(known_floor), float(seek_floor)

    if known_floor > seek_floor:
        floor_difference = known_floor - seek_floor
        height_difference = floor_difference * floor_height
        barometric_difference = height_difference / barometric_degree
        pressure_on_seek_floor = pressure_on_known_floor + barometric_difference
        print(
            f'Різниця поверхів = {known_floor} - {seek_floor} = {floor_difference}\n'
            f'Висотна різниця = {floor_difference} * {floor_height} = {height_difference}\n'
            f'Барометрична різниця = {height_difference} / {barometric_degree} = {round(barometric_difference, 2)}\n'
            f'Тиск на шуканому поверсі = {pressure_on_known_floor} + {round(barometric_difference, 2)} = {pressure_on_seek_floor}'
        )

    elif known_floor < seek_floor:
        floor_difference = seek_floor - known_floor
        height_difference = floor_difference * floor_height
        barometric_difference = height_difference / barometric_degree
        pressure_on_seek_floor = pressure_on_known_floor - barometric_difference
        print(
            f'Різниця поверхів = {seek_floor} - {known_floor} = {floor_difference}\n'
            f'Висотна різниця = {floor_difference} * {floor_height} = {height_difference}\n'
            f'Барометрична різниця = {height_difference} / {barometric_degree} = {round(barometric_difference, 2)}\n'
            f'Тиск на шуканому поверсі = {pressure_on_known_floor} - {round(barometric_difference, 2)} = {pressure_on_seek_floor}'
              )
    return round(pressure_on_seek_floor, 2)


def calc_height_of_building(pressure_floor1, pressure_floor2, barometric_degree=11):
    pressure_floor1, pressure_floor2, barometric_degree = coma_replace(pressure_floor1), \
                                                          coma_replace(pressure_floor2), coma_replace(barometric_degree)

    height_difference = 0

    if pressure_floor1 > pressure_floor2:
        pressure_difference = pressure_floor1 - pressure_floor2
        height_difference = pressure_difference * barometric_degree
        print(
            f'Барометрична різниця = {pressure_floor1} - {pressure_floor2} = {round(pressure_difference, 2)}'
            f'Висотна різниця = {round(pressure_difference, 2)} * {barometric_degree} = {round(height_difference, 2)}'
        )

    elif pressure_floor1 < pressure_floor2:
        pressure_difference = pressure_floor2 - pressure_floor1
        height_difference = pressure_difference * barometric_degree
        print(
            f'Барометрична різниця = {pressure_floor2} - {pressure_floor1} = {round(pressure_difference, 2)}\n'
            f'Висотна різниця = {round(pressure_difference, 2)} * {barometric_degree} = {round(height_difference, 2)}'
        )

    return round(height_difference, 2)


def permissible_height_residual(perimeter, n):
    perimeter, n = coma_replace(perimeter), coma_replace(n)
    perm_height_res = (0.04 * perimeter) / math.sqrt(n)
    print(
        f'Доп. вис. нев\'язка = (0.04 * {perimeter}) / квдр.кор.({n}) = {round(perm_height_res, 2)}'
    )
    return perm_height_res


def h2_having_h1_l_i(h1, h, i, l):
    h1, h, l, i = coma_replace(h1), coma_replace(h), coma_replace(l), coma_replace(i)
    h2 = h1 + h + i - l
    print(
        f'Вис. 2 точки = {h1} + {h} + {i} - {l} = {round(h2, 2)}'
    )
    return round(h2, 2)


def calc_zero_spot(kp, kl):
    kp, kl = convert_grad_min_secs_to_decimal(kp), convert_grad_min_secs_to_decimal(kl)
    z_spot = (kp + kl) / 2
    print(
        f'МО = (КП + КЛ) / 2'
    )
    z_spot_degrees, z_spot_minutes, z_spot_seconds = convert_decimal_degrees_to_degrees(z_spot)
    return z_spot_degrees, z_spot_minutes, z_spot_seconds


def calc_angle_having_mo_kp(zero_spot, kp):
    zero_spot, kp = convert_grad_min_secs_to_decimal(zero_spot), convert_grad_min_secs_to_decimal(kp)
    angle = (zero_spot - kp)
    print(
        'Кут падіння = МО - КП'
    )
    angle_degrees, angle_minutes, angle_seconds = convert_decimal_degrees_to_degrees(angle)
    return angle_degrees, angle_minutes, angle_seconds


def calc_angle_having_mo_kl(zero_spot, kl):
    zero_spot, kl = convert_grad_min_secs_to_decimal(zero_spot), convert_grad_min_secs_to_decimal(kl)
    angle = kl - zero_spot
    print(
        'Кут падіння = КЛ - МО'
    )
    angle_degrees, angle_minutes, angle_seconds = convert_decimal_degrees_to_degrees(angle)
    return angle_degrees, angle_minutes, angle_seconds


def angle_having_kl_kp(kl, kp):
    kl, kp = convert_grad_min_secs_to_decimal(kl), convert_grad_min_secs_to_decimal(kp)
    angle = (kl - kp) / 2
    print(
        'Кут падіння = (КЛ - КП) / 2'
    )
    angle_degrees, angle_minutes, angle_seconds = convert_decimal_degrees_to_degrees(angle)
    return angle_degrees, angle_minutes, angle_seconds


def h_having_d_v_i_l(d, v, i, l):
    d, i, l = coma_replace(d), coma_replace(i), coma_replace(l)
    v = convert_grad_min_secs_to_decimal(v)
    v = convert_decimal_deg_to_rad(v)
    d = d * (math.cos(v) ** 2)
    h = d * math.tan(v) + i - l
    v = convert_rad_to_decimal(v)
    degrees, minutes, seconds = convert_decimal_degrees_to_degrees(v)
    print(
        f'Гор. проекція = {d} * cos({degrees}°{minutes}\'{seconds}\'\') ** 2\n'
        f'Перевищення = {d} * tan({degrees}°{minutes}\'{seconds}\'\') + {i} - {l} = {round(h, 2)}'
    )
    return h


def absolute_lineal_residual_having_coords(x1, y1, xn, yn, practice_x, practice_y):
    x1, y1, xn, yn, practice_x, practice_y = coma_replace(x1), coma_replace(y1), coma_replace(xn), coma_replace(yn), \
                                             coma_replace(practice_x), coma_replace(practice_y)
    theory_x = xn - x1
    theory_y = yn - y1
    residual_x = practice_x - theory_x
    residual_y = practice_y - theory_y
    abs_lin_residual = math.sqrt(residual_x ** 2 + residual_y ** 2)
    print(
        f'ΣΔΧтеор = {xn} - {x1} = {round(theory_x, 2)}\n'
        f'ΣΔyтеор = {yn} - {y1} = {round(theory_y, 2)}\n'
        f'Нев\'зка по x = {practice_x} - {round(theory_x, 2)} = {round(residual_x, 2)}\n'
        f'Нев\'зка по y = {practice_y} - {round(theory_y, 2)} = {round(residual_y, 2)}\n'
        f'Абсолютна нев\'язка = корінь_квадр.({round(residual_x, 2)} ** 2 + {round(residual_y, 2)} ** 2) = {round(abs_lin_residual, 2)}'
    )
    return abs_lin_residual


def horizontal_projection_string(d, v):
    d = coma_replace(d)
    v = convert_grad_min_secs_to_decimal(v)
    v = convert_decimal_deg_to_rad(v)
    horizontal_projection = d * math.cos(v)
    v = convert_rad_to_decimal(v)
    degrees, minutes, seconds = convert_decimal_degrees_to_degrees(v)
    print(
        f'Гор. проєкція = {d} * cos({degrees}°{minutes}\'{seconds}\'\') = {round(horizontal_projection, 2)}'
    )
    return horizontal_projection


def horizontal_projection_rangefinder(d, v):
    d = coma_replace(d)
    v = convert_grad_min_secs_to_decimal(v)
    v = convert_decimal_deg_to_rad(v)
    horizontal_projection = d * (math.cos(v) ** 2)
    v = convert_rad_to_decimal(v)
    degrees, minutes, seconds = convert_decimal_degrees_to_degrees(v)
    print(
        f'Гор. проєкція = {d} * cos({degrees}°{minutes}\'{seconds}\'\') ** 2 = {round(horizontal_projection, 2)}'
    )
    return horizontal_projection


def height_residual(hst, hfn, pr_sum_excess):
    hst, hfn, pr_sum_excess = coma_replace(hst), coma_replace(hfn), coma_replace(pr_sum_excess)
    te_sum_excess = hfn - hst
    residual = pr_sum_excess - te_sum_excess
    print(
        f'Теор. сума перевищень = {hfn} - {hst} = {round(te_sum_excess, 2)}\n'
        f'Вис. нев\'язка = {pr_sum_excess} - {round(te_sum_excess, 2)} = {round(residual, 2)}'
    )
    return residual


def hor_proj_having_coords(x1, y1, xn, yn):
    x1, y1, xn, yn = coma_replace(x1), coma_replace(y1), coma_replace(xn), coma_replace(yn)
    difference_x = xn - x1
    difference_y = yn - y1
    horizontal_projection = math.sqrt(difference_x ** 2 + difference_y ** 2)
    print(
        f'Прирости x = {xn} - {x1} = {round(difference_x, 2)}\n'
        f'Прирости y = {yn} - {y1} = {round(difference_y, 2)}\n'
        f'Гор. проєкція = корінь_квадр({round(difference_x, 2)} ** 2 + {round(difference_y, 2)} ** 2) = {round(horizontal_projection, 2)}'
    )
    return horizontal_projection


def directory_angle(x1, y1, xn, yn):
    x1, y1, xn, yn = coma_replace(x1), coma_replace(y1), coma_replace(xn), coma_replace(yn)

    difference_x = xn - x1
    difference_y = yn - y1

    tan_r = difference_y / difference_x
    r = math.atan(tan_r)
    r = convert_rad_to_decimal(r)
    r_degrees, r_minutes, r_seconds = convert_decimal_degrees_to_degrees(r)

    print(
        f'Теор. сума x = {xn} - {x1} = {round(difference_x, 2)}\n'
        f'Теор. сума y = {yn} - {y1} = {round(difference_y, 2)}\n'
        f'tan(r) = {round(difference_y, 2)} / {round(difference_x, 2)} = {round(tan_r, 2)}\n'
        f'r = atan({round(tan_r, 2)}) = {r_degrees}°{r_minutes}\'{r_seconds}\'\''
    )

    angle_degrees, angle_minutes, angle_seconds = 0, 0, 0

    if difference_x > 0 and difference_y > 0:
        dir_angle = r
        angle_degrees, angle_minutes, angle_seconds = convert_decimal_degrees_to_degrees(dir_angle)
        print(f'Дирекційний = r = {r_degrees}°{r_minutes}\'{r_seconds}\'\'')

    elif difference_x < 0 and difference_y > 0:
        dir_angle = 180 - r
        angle_degrees, angle_minutes, angle_seconds = convert_decimal_degrees_to_degrees(dir_angle)
        print(f'Дирекційний = 180° - {r_degrees}°{r_minutes}\'{r_seconds}\'\' = {angle_degrees}°{angle_minutes}\'{angle_seconds}\'\'')

    elif difference_x < 0 and difference_y < 0:
        dir_angle = 180 + r
        angle_degrees, angle_minutes, angle_seconds = convert_decimal_degrees_to_degrees(dir_angle)
        print(f'Дирекційний = 180° + {r_degrees}°{r_minutes}\'{r_seconds}\'\' = {angle_degrees}°{angle_minutes}\'{angle_seconds}\'\'')

    elif difference_x > 0 and difference_y < 0:
        dir_angle = 360 - r
        angle_degrees, angle_minutes, angle_seconds = convert_decimal_degrees_to_degrees(dir_angle)
        print(f'Дирекційний = 360° - {r_degrees}°{r_minutes}\'{r_seconds}\'\' = {angle_degrees}°{angle_minutes}\'{angle_seconds}\'\'')

    return angle_degrees, angle_minutes, angle_seconds


def rumb_having_coords(x1, y1, xn, yn):
    x1, y1, xn, yn = coma_replace(x1), coma_replace(y1), coma_replace(xn), coma_replace(yn)

    difference_x = xn - x1
    difference_y = yn - y1

    tan_r = difference_y / difference_x
    r = abs(math.atan(tan_r))
    r = convert_rad_to_decimal(r)

    angle_degrees, angle_minutes, angle_seconds = convert_decimal_degrees_to_degrees(r)

    if difference_x > 0 and difference_y > 0:
        r = f'Пн.Сх {angle_degrees}°{angle_minutes}\'{angle_seconds}\'\''

    elif difference_x < 0 and difference_y > 0:
        r = f'Пд.Сх {angle_degrees}°{angle_minutes}\'{angle_seconds}\'\''

    elif difference_x < 0 and difference_y < 0:
        r = f'Пд.Зх {angle_degrees}°{angle_minutes}\'{angle_seconds}\'\''

    elif difference_x > 0 and difference_y < 0:
        r = f'Пн.Зх {angle_degrees}°{angle_minutes}\'{angle_seconds}\'\''

    print(
        f'Теор. сума x = {xn} - {x1} = {round(difference_x, 2)}\n'
        f'Теор. сума y = {yn} - {y1} = {round(difference_y, 2)}\n'
        f'tan(r) = {round(difference_y, 2)} / {round(difference_x, 2)} = {round(tan_r, 2)}\n'
        f'r = atan({round(tan_r, 2)}) = {angle_degrees}°{angle_minutes}\'{angle_seconds}\'\''
    )

    return r


def excess_having_d_v_i_l(d, v, i, l):
    d, i, l = coma_replace(d), coma_replace(i), coma_replace(l)
    v = convert_grad_min_secs_to_decimal(v)
    v = convert_decimal_deg_to_rad(v)
    h = d * math.tan(v) + i - l
    print(
        f'Перевищення = {d} * tan(кут) + {i} - {l} = {round(h, 2)}'
    )
    return h


def relative_residual(x1, y1, xn, yn, xpr, ypr, p):
    x1, y1, xn, yn, xpr, ypr, p = coma_replace(x1), coma_replace(y1), coma_replace(xn), coma_replace(yn), \
                                  coma_replace(xpr), coma_replace(ypr), coma_replace(p)

    difference_x = xn - x1
    difference_y = yn - y1
    residual_x = xpr - difference_x
    residual_y = ypr - difference_y

    abs_residual = math.sqrt((residual_x ** 2) + (residual_y ** 2))
    abs_residual = round(abs_residual, 2)
    rel_residual = p / abs_residual

    print(
        f'Теор сума x = {xn} - {x1} = {round(difference_x,2)}\n'
        f'Теор сума y = {yn} - {y1} = {round(difference_y, 2)}\n'
        f'Нев\'язка x = {xpr} - {round(difference_x, 2)} = {round(residual_x, 2)}\n'
        f'Нев\'язка y = {ypr} - {round(difference_y, 2)} = {round(residual_y, 2)}\n'
        f'Абс. нев. = корінь_квдр({round(residual_x, 2)} ** 2 + {round(residual_y, 2)} ** 2) = {round(abs_residual, 2)}\n'
        f'Відносна нев\'зка = 1 / ({p} / {round(abs_residual, 2)}) = 1 / {round(rel_residual)}'
    )

    return rel_residual
