# -*- coding: utf-8 -*-
# _author: zb
# date: 19-4-27 下午7:29


# 插入排序
def insert_sort(li):
    n = len(li)
    for i in range(1, n):
        for j in range(0, i):
            if li[i] < li[j]:
                li[i], li[j] = li[j], li[i]
    return li


if __name__ == '__main__':
    li = [23, 45, 67, 24, 66, 34, 67, 3578, 56]
    print(li)
    result = insert_sort(li)
    print(result)
