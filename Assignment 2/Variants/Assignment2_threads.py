import numpy as np
import skimage.io as sk
from math import *
import threading as th


# temp = mp.s
img = sk.imread('Italy50.png')
rows, cols, rgb = np.shape(img)
imgArr = np.asarray(img)
ansImgArr = np.zeros(shape=(rows, cols, 3), dtype=np.uint8)


def euclidean_distance(x, y):
    return sqrt(sum(pow(a - b, 2) for a, b in zip(x, y)))


def manhattan_distance(x, y):
    return sum(abs(x[i] - y[i]) for i in range(3))


def iswhite(point):
    return point[0] == point[1] == point[2]


def isblue(point):
    return point[1] < point[2]


def isgreen(point):
    return point[1] > point[2]


def findnearest(r, c, arr, tr, tc):
    min_dis = 10000.0
    rr = 0
    rc = 0
    for sr in range(r, tr):
        for sc in range(c, tc):
            if not iswhite(arr[sr][sc]):
                dist = manhattan_distance(arr[r][c], arr[sr][sc])
                if min_dis > dist:
                    rr = sr
                    rc = sc
                    min_dis = dist
    return rr, rc


def work(t_row, t_cols, s_rows, s_cols):
    for i in range(s_rows, t_row):
        for j in range(s_cols, t_cols):
            if iswhite(imgArr[i][j]):
                rrow, rcol = findnearest(i, j, imgArr, rows, cols)
                if rrow < 0 or rcol < 0:
                    break
                print("near found", i, j)
                ansImgArr[i][j] = imgArr[rrow][rcol]
            else:
                ansImgArr[i][j] = imgArr[i][j]
    # f_name = 'result/'+str(s_rows)+'.png'
    # sk.imsave(f_name, ansImgArr)


def p_start():
    print("it's started")


if __name__ == "__main__":
    thr = 10
    f_r = int(rows/thr)
    f_c = int(cols/thr)
    t1 = th.Thread(target=p_start)
    t = [t1] * thr
    for t_ind in range(thr):
        t[t_ind] = th.Thread(target=work, args=(f_r * t_ind, f_c * t_ind, f_r * (t_ind - 1), f_c * (t_ind - 1),))
        t[t_ind].start()

    for th in t:
        th.join()

    print("done")
    sk.imsave('result/result.png', ansImgArr)
