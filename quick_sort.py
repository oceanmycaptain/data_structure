# -*- coding: utf-8 -*-
# _author: zb
# date: 19-4-27 下午7:47


def quick_sort(li, start, end):
    """快速排序"""
    # 设定基准元素必须是自己的第一个
    if start > end:
        return

    mid = li[start] # 需要将基准确定到
    low = start
    high = end

    while low < high:
        while li[high] >= mid and low < high:
            high -= 1
        li[low] = li[high]

        while li[low] < mid and low < high:
            low += 1
        li[high] = li[low]

    li[high] = mid

    quick_sort(li, start, low - 1)
    quick_sort(li, low + 1, end)

if __name__ == '__main__':
    li = [23, 45, 67, 24, 66, 34, 67, 3578, 56]
    print(li)
    quick_sort(li, 0, len(li) - 1)
    print(li)
