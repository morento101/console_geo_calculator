import math


def coma_replace(s):
    s = str(s)
    if ',' in s:
        s = s.replace(',', '.')
    return float(s)


def round_2(ans):
    return round(ans, 2)


def result(res):
    print(f'Результат: {round_2(res)}мм')


def permissible_residual_technical_leveling(length):
    perm_res = 50 * math.sqrt(length)
    perm_res = math.ceil(perm_res)
    result(perm_res)


def permissible_residual_leveling_4class(length):
    perm_res = 20 * math.sqrt(length)
    perm_res = math.ceil(perm_res)
    result(perm_res)


def device_horizon(h, a):
    dev_horizon = h + a
    result(dev_horizon)


def intermediate_point_height(h, a, c):
    dev_horizon = h + a
    inter_point_h = dev_horizon - c
    result(inter_point_h)
