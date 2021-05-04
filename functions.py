import math

ONE_RAD = 0.01745329252


def coma_replace(s):
    s = str(s)
    if ',' in s:
        s = s.replace(',', '.')
    return float(s)


def readout_convert_to_metres(readout):
    if len(readout) == 4:
        readout = readout[0] + '.' + readout[1:]
    return float(readout)


def calc_asec(angle):
    return math.acos(1 / angle)


def calc_sec(angle):
    return 1 / math.cos(angle)


def convert_grad_min_secs_to_decimal(string):
    string = string.split(' ')
    if len(string) == 3:
        degrees, minutes, seconds = string[0], string[1], string[2]
        decimal_degrees = (float(degrees) + float(minutes) / 60 + float(seconds) / 3600) * ONE_RAD
        return decimal_degrees

    elif len(string) == 2:
        degrees, minutes = string[0], string[1]
        decimal_degrees = (float(degrees) + float(minutes) / 60) * ONE_RAD
        return decimal_degrees

    elif len(string) == 1:
        degrees = string[0]
        decimal_degrees = float(degrees) * ONE_RAD
        return decimal_degrees

    else:
        print('НЕПРАВИЛЬНИЙ ФОРМАТ!!!')


def permissible_residual_leveling_4class(length):
    length = coma_replace(length)
    perm_res = 20 * math.sqrt(length)
    perm_res = math.ceil(perm_res)
    return perm_res


def permissible_residual_technical_leveling(length):
    length = coma_replace(length)
    perm_res = 50 * math.sqrt(length)
    perm_res = math.ceil(perm_res)
    return perm_res


def device_horizon(h, a):
    a = readout_convert_to_metres(a)
    h, a = coma_replace(h), coma_replace(a)
    dev_horizon = h + a
    return round(dev_horizon, 3)


def intermediate_point_height(h, a, c):
    a, c = readout_convert_to_metres(a), readout_convert_to_metres(c)
    h, a, c = coma_replace(h), coma_replace(a), coma_replace(c)
    dev_horizon = h + a
    inter_point_h = dev_horizon - c
    return round(inter_point_h, 3)


def project_height2(h1, i, d):
    h1, i, d = coma_replace(h1), coma_replace(i), coma_replace(d)
    h2 = (i * d) + h1
    return round(h2, 2)


def calc_slope(h1, h2, d):
    h1, h2, d = coma_replace(h1), coma_replace(h2), coma_replace(d)
    slope = ((h2 - h1) / d) * 1000
    return round(slope)


def calc_tan_having_radius_bisector(r, b):
    r, b = coma_replace(r), coma_replace(b)
    angle = 2 * calc_asec((b / r) + 1)
    tangent = r * math.tan(angle / 2)
    return round(tangent, 2)


def calc_tan_having_curve_measure(c, m):
    c, m = coma_replace(c), coma_replace(m)
    tangent = (m + c) / 2
    return round(tangent, 2)


def calc_tan_having_angle_radius(angle, radius):
    angle, radius = convert_grad_min_secs_to_decimal(angle), coma_replace(radius)
    tangent = radius * math.tan(angle / 2)
    return round(tangent, 2)


def calc_bisector_having_radius_angle(radius, angle):
    angle, radius = convert_grad_min_secs_to_decimal(angle), coma_replace(radius)
    bisector = radius * (calc_sec(angle / 2) - 1)
    return round(bisector, 2)


def angle_having_radius_tangent(radius, tangent):
    radius, tangent = coma_replace(radius), coma_replace(tangent)
    angle = 2 * math.atan(tangent / radius)
    return angle


def convert_decimal_degrees_to_degrees(angle):
    degrees = int(angle)
    minutes = int((angle - degrees) * 60)
    seconds = round((angle - degrees - (minutes / 60)) * 3600)
    return f'{degrees}°{minutes}\'{seconds}\'\''


def calc_bisector_having_tangent_radius(tangent, radius):
    tangent, radius = coma_replace(tangent), coma_replace(radius)
    angle = 2 * math.atan(tangent / radius)
    bisector = radius * (calc_sec(angle / 2) - 1)
    return round(bisector, 2)


def distance_from_0work_by_x(h1, h2, d):
    h1, h2, d = coma_replace(h1), coma_replace(h2), coma_replace(d)
    x = (h1 * d) / (h1 + h2)
    return round(x, 2)


def distance_from_0work_by_y(h1, h2, d):
    h1, h2, d = coma_replace(h1), coma_replace(h2), coma_replace(d)
    x = (h2 * d) / (h1 + h2)
    return round(x, 2)


def curve_having_radius_angle(radius, angle):
    radius, angle = coma_replace(radius), convert_grad_min_secs_to_decimal(angle)
    curve = radius * ((math.pi * angle) / (180 * ONE_RAD))
    return round(curve, 2)


def curve_having_tangent_measure(tangent, measure):
    tangent, measure = coma_replace(tangent), coma_replace(measure)
    curve = 2 * tangent - measure
    return round(curve, 2)


def calc_measure_having_radius_angle(radius, angle):
    radius, angle = coma_replace(radius), convert_grad_min_secs_to_decimal(angle)
    measure = radius * ((2 * math.tan(angle / 2)) - ((math.pi * angle) / (180 * ONE_RAD)))
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

    elif known_floor < seek_floor:
        floor_difference = seek_floor - known_floor
        height_difference = floor_difference * floor_height
        barometric_difference = height_difference / barometric_degree
        pressure_on_seek_floor = pressure_on_known_floor - barometric_difference

    return round(pressure_on_seek_floor, 2)


def calc_height_of_building(pressure_floor1, pressure_floor2, barometric_degree=11):
    pressure_floor1, pressure_floor2, barometric_degree = coma_replace(pressure_floor1), \
                                                          coma_replace(pressure_floor2), coma_replace(barometric_degree)

    height_difference = 0

    if pressure_floor1 > pressure_floor2:
        pressure_difference = pressure_floor1 - pressure_floor2
        height_difference = pressure_difference * barometric_degree

    elif pressure_floor1 < pressure_floor2:
        pressure_difference = pressure_floor2 - pressure_floor1
        height_difference = pressure_difference * barometric_degree

    return round(height_difference, 2)


def permissible_height_residual(perimeter, n):
    perimeter, n = coma_replace(perimeter), coma_replace(n)
    perm_height_res = (0.04 * perimeter) / math.sqrt(n)
    return perm_height_res


def h2_having_h1_l_i(h1, h, i, l):
    h1, h, l, i = coma_replace(h1), coma_replace(h), coma_replace(l), coma_replace(i)
    print(h1, h, i, l)
    h2 = h1 + h + i - l
    print(h1, h2, h, i, l)
    return round(h2, 2)
