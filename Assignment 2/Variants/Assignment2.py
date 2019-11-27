from math import *
import numpy as np
import skimage.io as sk
import copy as cpy
import glob


def p_start():
    print("it's started")


image_list = []
for filename in glob.glob('/*.png'):  # assuming gif
    image_list.append(filename)
proc = 10
thr = 2


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


def find_nearest(r, c, arr, st_r, end_r, pr, pc, t_num):
    pnt = [0, 0, 0]
    result = [pnt]
    for sr in range(st_r, end_r):
        for sc in range(0, cols):
            if not iswhite(arr[sr][sc]):
                pnt[0] = sr
                pnt[1] = sc
                pnt[2] = manhattan_distance([r, c], [sr, sc])
                temp_pnt = cpy.deepcopy(pnt)
                result.append(temp_pnt)
    result.sort(key=lambda x: x[2])
    Results[pr][pc].append(result)


def work(s_row, s_col, t_rows, t_cols, pr_num, pc_num):
    sel = list()
    for i in range(s_row, t_rows):
        for j in range(s_col, t_cols):
            if iswhite(imgArr[i][j]):
                find_nearest()
            else:
                ansImgArr[i][j] = imgArr[i][j]
    f_name = 'result/' + str(s_row) + '.png'
    sk.imsave(f_name, ansImgArr)


def main():
    for image in image_list:



    p1 = mp.Process(target=p_start)
    p = [[p1] * proc] * proc
    for pr_ind in range(proc):
        for pc_ind in range(proc):
            p[pr_ind][pc_ind] = mp.Process(target=work, args=())
            p[pr_ind][pc_ind].start()

    for pro in p:
        for pi in pro:
            pi.join()

    print("done")
    sk.imsave('result/result.png', ansImgArr)


if __name__ == "__main__":
    main()
