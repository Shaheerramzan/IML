import multiprocessing as mp
from math import *
import queue as qu
import numpy as np
import skimage.io as sk
import copy as cpy


def p_start():
    print("it's started")

# GREEN is 0
# BLUE is 1


proc = 10
thr = 2
s_temp = list()
Results = [[s_temp] * proc] * proc
img = sk.imread('Italy50.png')
rows, cols, rgb = np.shape(img)
# cols = 200
# rows = 100
imgArr = np.asarray(img)
ansImgArr = np.zeros(shape=(rows, cols, 3), dtype=np.uint8)
f_r = int(rows / proc)
f_c = int(cols / proc)
T = 1


def euclidean_distance(x, y):
    return sqrt(sum(pow(a - b, 2) for a, b in zip(x, y)))


def manhattan_distance(x, y):
    return sum(abs(x[i] - y[i]) for i in range(2))


def iswhite(point):
    return point[0] == point[1] == point[2]


def isblue(point):
    return point[1] < point[2]


def isgreen(point):
    return point[1] > point[2]


def produce_child(r, c, visit):
    c = [0, 0] * 4
    # c[0][0] = [r-1, c]
    # c[1]
    # if visit[r][c]:


def find_nearest(r, c):
    visited = np.zeros(shape=(rows, cols), dtype=np.bool)
    q = qu.Queue(T)
    child =[0, 0] * 4
    point = [r, c]
    q.put([r, c])
    q.put([-1, -1])
    finals = [0, 0] * T
    limit = 1
    visited[r][c] = True
    while True:
        while point != [-1, -1]:
            point = q.get()
            if point[2] == -1:
                pass
            else:
                q.put([-1, -1])
                pass

        if q.empty():
            break

    return finals


def decide_final(lst):
    fn = lst[0]
    g, b = 0, 0
    for pnt in lst:
        if pnt[2]:
            g += 1
        else:
            b += 1
    return g < b


def work(s_row, s_col, t_rows, t_cols, pr_num, pc_num):
    sel = list()
    for i in range(s_row, t_rows):
        for j in range(s_col, t_cols):
            if iswhite(imgArr[i][j]):
                kn = find_nearest(i, j)
                row, col, flag = decide_final(kn)
                ansImgArr[i][j] = imgArr[row][col]
                if isgreen(imgArr[row][col]):
                    print(f'done with row {i} col {j} :  green selected.')
                if isblue(imgArr[row][col]):
                    print(f'done with row {i} col {j} :  blue selected.')
            else:
                ansImgArr[i][j] = imgArr[i][j]
    f_name = 'result/' + str(s_row) + '.png'
    sk.imsave(f_name, ansImgArr)


def main():
    p1 = mp.Process(target=p_start)
    p = [[p1] * proc] * proc
    for pr_ind in range(proc):
        for pc_ind in range(proc):
            p[pr_ind][pc_ind] = mp.Process(target=work, args=(f_r * pr_ind, f_c * pc_ind, f_r * (pr_ind + 1), f_c * (pc_ind + 1), pr_ind, pc_ind,))
            p[pr_ind][pc_ind].start()

    for pro in p:
        for process in pro:
            process.join()

    print("done")
    sk.imsave('result/result.png', ansImgArr)


if __name__ == "__main__":
    main()
