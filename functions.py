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
    return math.acos(1/angle)


def convert_grad_min_secs_to_decimal(string):
    string = string.split(' ')
    if len(string) == 3:
        degrees, minutes, seconds = string[0], string[1], string[2]
        decimal_degrees = float(degrees) + float(minutes) / 60 + float(seconds) / 3600
        return decimal_degrees

    elif len(string) == 2:
        degrees, minutes = string[0], string[1]
        decimal_degrees = float(degrees) + float(minutes) / 60
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
    tangent = radius * math.tan((angle * ONE_RAD) / 2)
    return round(tangent, 2)
