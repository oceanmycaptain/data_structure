# -*- coding: utf-8 -*-
# _author: zb
# date: 19-4-27 下午8:13


# 希尔算法
def shell_sort(li):
    n = len(li)
    gap = n // 2
    while gap > 0:
        print('*'*10)
        for i in range(gap, n):
            j = i
            while li[j - gap] > li[j] and j >= gap:
                li[j], li[j - gap] = li[j - gap], li[j]
                j -= gap
                print(li)
        gap = gap // 2

    return li


if __name__ == '__main__':
    li = [23, 45, 67, 24, 66, 34, 67, 3578, 56]
    print(li)
    result = shell_sort(li)
    print(result)
