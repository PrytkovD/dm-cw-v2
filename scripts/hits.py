import numpy as np


def task1_adj_mat():
    M = np.array([
        [1, 1, 1],
        [1, 0, 1],
        [0, 1, 1]
    ])
    return M


def task2_adj_mat(m: int):
    M = np.zeros((m, m))

    for i in range(m):
        for j in range(m):
            M[i][j] = int(i == j == 0 or j == i + 1)

    return M


def task3_adj_mat(n: int):
    m = sum(pow(2, i - 1) for i in range(1, n + 1))

    M = np.empty((m, m))

    for i in range(m):
        for j in range(m):
            M[i][j] = int(i == j == 0 or j == 2 * i + 1 or j == 2 * i + 2)

    return M


if __name__ == '__main__':
    n = 2
    m = 5

    # M = task1_adj_mat()
    # M = task2_adj_mat(m)
    M = task3_adj_mat(n)
    MT = np.transpose(M)

    m = len(M)

    print(m)

    MxMT = np.matmul(M, MT)
    MTxM = np.matmul(MT, M)

    h = np.ones((m, 1))
    a = np.ones((m, 1))

    for i in range(1000):
        u = np.matmul(MxMT, h)
        v = np.matmul(MTxM, a)
        h = u / np.linalg.norm(u)
        a = v / np.linalg.norm(v)

    print(', '.join('{:.8f}'.format(float(i)) for i in h))
    print(', '.join('{:.8f}'.format(float(i)) for i in a))
