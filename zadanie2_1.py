a_list = [1, 4, 3, 7, 5]
b_list = [6, 5, 6, 5, 6, 6]


def better_list(a_list, b_list):
    tmp1 = [i for idx, i in enumerate(a_list) if idx % 2 == 0]
    tmp2 = [i for idx, i in enumerate(b_list) if idx % 2 == 1]

    return tmp1 +tmp2


print(better_list(a_list, b_list))