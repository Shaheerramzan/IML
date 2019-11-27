from math import *
import numpy as np
import skimage.io as sk
import copy as cpy
import glob


def euclidean_distance(x, y):
    return sqrt(sum(pow(a - b, 2) for a, b in zip(x, y)))


def manhattan_distance(x, y):
    return sum(abs(a - b) for a, b in zip(x, y))


def iswhite(point):
    return point[0] == point[1] == point[2]


def isblue(point):
    return point[1] < point[2]


def isgreen(point):
    return point[1] > point[2]


def def_limits(wr, wc, t_r, t_c, lim):
    sr, er, sc, ec = 0, 0, 0, 0
    if 5 <= lim <= 9:
        sr, er, sc, ec = wr - 15, wr + 15, wc - 15, wc + 15
    else:
        sr, er, sc, ec = wr - 10, wr + 10, wc - 10, wc + 10
    if sr < 0:
        sr = 0
    if er > t_r:
        er = t_r
    if sc < 0:
        sc = 0
    if ec > t_c:
        ec = t_c
    return sr, er, sc, ec


def find_k_nearest(arr, knn, f, r, c, t_row, t_col):
    pnt = [0, 0, 0]
    point = [0, 0, 1000]
    k_array = [point] * knn
    s_row, e_row, s_col, e_col = def_limits(r, c, t_row, t_col, knn)
    ite = 0
    for rw in range(s_row, e_row):
        for cl in range(s_col, e_col):
            p = arr[rw][cl]
            if not iswhite(p):
                pnt[0] = rw
                pnt[1] = cl
                if f == 0:
                    pnt[2] = manhattan_distance([r, c], [rw, cl])
                else:
                    pnt[2] = euclidean_distance([r, c], [rw, cl])
                if ite == knn:
                    ite = knn - 1
                    if knn > 1:
                        k_array.sort(key=lambda x: x[2])
                    last = k_array[ite]
                    if last[2] > pnt[2]:
                        del last
                        k_array[ite] = cpy.deepcopy(pnt)
                        ite += 1
                    else:
                        ite += 1
                else:
                    k_array[ite] = cpy.deepcopy(pnt)
                    ite += 1
    return k_array


def selected_color(a, near):
    g, b = 0, 0
    for inst in near:
        nr = inst[0]
        nc = inst[1]
        pt = a[nr][nc]
        if isgreen(pt):
            g += 1
        if isblue(pt):
            b += 1
    if g > b:
        return [184, 236, 168]
    else:
        return [105, 169, 255]


def work(array, kn, fun, t_rows, t_cols, per):
    answer = np.zeros(shape=(t_rows, t_cols, 3), dtype=np.uint8)
    for row in range(t_rows):
        for col in range(t_cols):
            point = array[row][col]
            if iswhite(point):
                k_nearest = find_k_nearest(array, kn, fun, row, col, t_rows, t_cols)
                answer[row][col] = selected_color(array, k_nearest)
                # print(f'Done for {row} row and {col} column')
            else:
                answer[row][col] = array[row][col]
    if fun == 0:
        f_name = 'manh'
    else:
        f_name = 'eucl'
    name = 'Italy_' + str(per * 10) + '-' + f_name + '-' + str(kn)
    sk.imsave('result/' + str(name) + '.png', answer)


image_list = []
for filename in glob.glob('images/*.png'):  # assuming gif
    image_list.append(filename)
image_list.sort()

K = [1, 3, 5, 7, 9]
percent = 1

for image in image_list:
    img = sk.imread(image)
    imgArr = np.asarray(img)
    rows, cols, rgb = np.shape(img)
    for k in K:
        print(f'for {image} and k is: {k} ')
        work(imgArr, k, 0, rows, cols, percent)
        work(imgArr, k, 1, rows, cols, percent)
    percent += 1
