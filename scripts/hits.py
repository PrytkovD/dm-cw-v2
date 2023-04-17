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


def main():
    task = input("Which task to run? (1, 2, or 3)")

    if task == '1':
        M = task1_adj_mat()
    elif task == '2':
        n = int(input("How many vertices are in the graph?"))
        M = task2_adj_mat(n)
    elif task == '3':
        n = int(input("How many levels are in the tree?"))
        M = task3_adj_mat(n)
    else:
        return

    MT = np.transpose(M)

    MxMT = np.matmul(M, MT)
    MTxM = np.matmul(MT, M)

    m = len(M)
    h = np.ones((m, 1))
    a = np.ones((m, 1))

    for i in range(1000):
        u = np.matmul(MxMT, h)
        v = np.matmul(MTxM, a)
        h = u / np.linalg.norm(u)
        a = v / np.linalg.norm(v)

    print('h = ({})'.format(', '.join('{:.8f}'.format(float(i)) for i in h)))
    print('a = ({})'.format(', '.join('{:.8f}'.format(float(i)) for i in a)))


if __name__ == '__main__':
    main()
