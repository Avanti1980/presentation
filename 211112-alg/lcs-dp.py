#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from bisect import bisect_left

import numpy as np


def restore_lcs(b, x, i, j, lcs):
    if i == -1 or j == -1:
        return
    if b[i, j] == -1:
        restore_lcs(b, x, i-1, j-1, lcs)
        lcs.append(x[i])
    elif b[i, j] == -2:
        restore_lcs(b, x, i-1, j, lcs)
    else:
        restore_lcs(b, x, i, j-1, lcs)


n = 20

np.random.seed(1)
x = np.random.permutation(n) + 1  # 生成第一个排列
print("X: %s" % x)

np.random.seed(2)
y = np.random.permutation(n) + 1  # 生成第二个排列
print("Y: %s" % y)

b = np.zeros([n, n])
c = np.zeros([n+1, n+1])

for i in range(1, n+1):
    for j in range(1, n+1):
        if x[i-1] == y[j-1]:
            c[i, j] = c[i-1, j-1] + 1  # 如果当前两个子串的最后一个字符相同
            b[i-1, j-1] = -1
        elif c[i-1, j] >= c[i, j-1]:
            c[i, j] = c[i-1, j]
            b[i-1, j-1] = -2
        else:
            c[i, j] = c[i, j-1]
            b[i-1, j-1] = -3

lcs = []
restore_lcs(b, x, n-1, n-1, lcs)
print('LCS: %s' % lcs)

dict = {key: value for key, value in zip(x, range(1, n+1))}  # X -> [1:n]
print("sigma: %s" % dict)

x2 = [dict[i] for i in x]
print("X: %s -> %s" % (x, x2))

y2 = [dict[i] for i in y]
print("Y: %s -> %s" % (y, y2))

lcs2 = [dict[i] for i in lcs]
print('LCS: %s -> %s' % (lcs, lcs2))

x = y2
print('X: %s' % x)

d = np.ones(n, dtype=np.int32)
p = -1 * np.ones(n, dtype=np.int32)
for i in range(1, n):
    for j in range(i):
        if y2[j] < y2[i] and d[i] < d[j] + 1:
            d[i] = d[j] + 1
            p[i] = j
print('d: %s' % d)

lis_len_index = np.argmax(d)
lis = [y2[lis_len_index]]
pos = p[lis_len_index]
while pos != -1:
    lis.append(y2[pos])
    pos = p[pos]

lis.reverse()
print('LIS: %s' % lis)

e = []
p = -1 * np.ones(n, dtype=np.int32)
for i in range(n):
    j = bisect_left(e, x[i])
    if j == len(e):
        if j > 0:
            p[i] = e[-1]
        e.append(x[i])
    else:
        e[j] = x[i]
        p[i] = e[j-1]
    print("iteration %d: e = %s" % (i+1, e))

dict = {key: value for key, value in zip(x, range(n))}
lis = []
pre = e[-1]
for i in range(len(e)):
    lis.append(pre)
    pre = p[dict[pre]]

lis.reverse()
print('LIS: %s' % lis)
