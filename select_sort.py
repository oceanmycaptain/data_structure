# -*- coding: utf-8 -*-
# _author: zb
# date: 19-4-27 下午6:38


# 选择排序(从小到大排序)
def select_sort(li):
    n = len(li)
    # 假设最大的数字的序列在第一个
    for j in range(0, n-1):
        max_index = 0
        for i in range(0, n - j):
            if li[i] > li[max_index]:
                max_index = i # 取得最大的值的索引
        li[max_index],li[n-j-1] = li[n-j-1],li[max_index]
    return li


if __name__ == '__main__':
    li = [23, 45, 67, 24, 66, 34, 67, 3578, 56,13]
    print(li)
    result = select_sort(li)
    print(result)
