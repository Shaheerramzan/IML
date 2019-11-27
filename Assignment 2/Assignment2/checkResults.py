import numpy as np
import skimage.io as sk
import glob


def isblue(point):
    return point[1] < point[2]


def isgreen(point):
    return point[1] > point[2]


TP, TN, FP, FN = 0, 0, 0, 0
img = sk.imread('Italy.png')
ItalyArr = np.asarray(img)
rows, cols, rgb = np.shape(ItalyArr)

for filename in glob.glob('result/*.png'):
    imgC = sk.imread(filename)
    cmpArr = np.asarray(imgC)
    n = filename.split('.')
    na = n[0].split('/')
    name = 'text/' + na[1] + '.txt'
    f = open(name, 'w')
    for row in range(rows):
        for col in range(cols):
            if isgreen(ItalyArr[row][col]) and isgreen(cmpArr[row][col]):
                TP += 1
            if isblue(ItalyArr[row][col]) and isblue(cmpArr[row][col]):
                TN += 1
            if isblue(ItalyArr[row][col]) and isgreen(cmpArr[row][col]):
                FP += 1
            if isgreen(ItalyArr[row][col]) and isblue(cmpArr[row][col]):
                FN += 1
    f.write(f'TP is: {TP}\n')
    f.write(f'TN is: {TN}\n')
    f.write(f'FP is: {FP}\n')
    f.write(f'FN is: {FN}\n')
    f.write(f'Sensitivity is: {TP/(TP + FN)}\n')
    f.write(f'Specificity is: {TN/(TN + FP)}\n')
    f.write(f'Accuracy is: {(TN + TP)/(TN + TP + FN + FP)}\n')
    f.close()
    del n
    del na
    del f
    del name
    del imgC
    del cmpArr

