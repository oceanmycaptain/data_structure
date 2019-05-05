# -*- coding: utf-8 -*-
# _author: zb
# date: 19-4-27 下午6:24


# 冒泡排序
def bubble_sort(li):
    n = len(li)
    for j in range(0, n - 1):
        count = 0  # 用于处理已经排列好的数据
        for i in range(0, n - 1 - j):
            if li[i] > li[i + 1]:
                li[i], li[i + 1] = li[i + 1], li[i]
                count += 1
        if count == 0:
            break
    return li


if __name__ == '__main__':
    li = [23, 45, 67, 24, 66, 34, 67, 3578, 56]
    print(li)
    result = bubble_sort(li)
    print(result)
