import numpy as np


def win_checker(m):
    result = 0
    # print(m)
    a_1 = m
    a_2 = np.fliplr(m)
    # print(a_2)
    a = a_1.sum(axis=0)
    a1 = int(a[0])
    a2 = int(a[1])
    a3 = int(a[2])
    b = a_1.sum(axis=1)
    b1 = int(b[0])
    b2 = int(b[1])
    b3 = int(b[2])
    main_diag = a_1.diagonal()
    second_diag = a_2.diagonal()
    c = int(main_diag.sum())
    d = int(second_diag.sum())
    # print(a, b, c, d)
    if a1 == 3 or a2 == 3 or a3 == 3 or b1 == 3 or b2 == 3 or b3 == 3 or c == 3 or d == 3:
        # print("Circle WINS")
        result = 1
    elif a1 == -3 or a2 == -3 or a3 == -3 or b1 == -3 or b2 == -3 or b3 == -3 or c == -3 or d == -3:
        # print("Cross WINS")
        result = -1

    return result
