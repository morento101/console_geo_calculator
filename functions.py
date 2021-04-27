import math


def permissible_residual_technical_leveling(len):
    perm_res = 50 * math.sqrt(len)
    perm_res = math.ceil(perm_res)
    print(f'Результат: {perm_res}мм')


def permissible_residual_leveling_4class(len):
    perm_res = 20 * math.sqrt(len)
    perm_res = math.ceil(perm_res)
    print(f'Результат: {perm_res}мм')


def intermediate_point_height(h, a):
    inter_height = h + a
    print(inter_height)
