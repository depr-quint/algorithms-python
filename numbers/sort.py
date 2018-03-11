from math import floor
from random import shuffle

from numbers import utilities as util

#--------------- ~ ---------------#

def insertion(a):
    for i in range(len(a)):
        for j in range(i, 0, -1):
            if (util.less(a[j], a[j - 1])):
                util.exchange(a, j, j - 1);
            else: break

#--------------- ~ ---------------#

def selection(a):
    for i in range(len(a)):
        m = i;
        for j in range(i + 1, len(a)):
            if (util.less(a[j], a[m])):
                m = j;
        util.exchange(a, i, m);

#--------------- ~ ---------------#

def merge(a):
    merge_sort(a, 0, len(a) - 1)

def merge_sort(a, low, high):
    if (low < high):
        mid = floor((low + (high - 1)) / 2)
        merge_sort(a, low, mid)
        merge_sort(a, mid + 1, high)
        merge_combine(a, low, mid, high)

def merge_combine(a, low, mid, high):
    l, r = mid - low + 1, high - mid
    left, right = [0] * l, [0] * r

    for i in range(0 , l): left[i] = a[low + i]
    for j in range(0 , r): right[j] = a[mid + 1 + j]

    i, j, k = 0, 0, low

    while (i < l and j < r):
        if left[i] <= right[j]:
            a[k], i = left[i], i + 1
        else:
            a[k], j = right[j], j + 1
        k += 1
    while (i < l):
        a[k], i, k = left[i], i + 1, k + 1
    while (j < r):
        a[k], j, k = right[j], j + 1, k + 1

#--------------- ~ ---------------#

def quick(a):
    shuffle(a)
    quick_sort(a, 0, len(a) - 1)

def quick_sort(a, low, high):
    if (low < high):
        j = quick_partition(a, low, high)
        quick_sort(a, low, j - 1)
        quick_sort(a, j + 1, high)

def quick_partition(a, low, high):
    p, l, r = a[low], low + 1, high

    done = False
    while not done:
        while l <= r and a[l] <= p: l += 1
        while r >= l and a[r] >= p: r -= 1
        if r < l: done = True
        else: util.exchange(a, l, r)
    util.exchange(a, low, r)

    return r

#--------------- ~ ---------------#

def tim(a):
    run = 32
    for low in range(0, len(a), run):
        mid = util.min(low + 31, len(a) - 1)
        tim_insertion(a, low, mid)
    size = run
    while (size < len(a)):
        for low in range(0, len(a), 2 * size):
            mid = util.min(low + size - 1, len(a) - 1)
            high = util.min(low + 2 * size - 1, len(a) - 1)
            merge_combine(a, low, mid, high)
        size *= 2

def tim_insertion(a, low, high):
    for i in range(low, high + 1):
        for j in range(i, low, -1):
            if (util.less(a[j], a[j - 1])):
                util.exchange(a, j, j - 1);
            else: break

#--------------- ~ ---------------#

def bubble(a):
    for i in range(len(a)):
        for j in range(0, len(a) - i - 1):
            if (a[j] > a[j + 1]):
                util.exchange(a, j, j + 1)

#--------------- ~ ---------------#

def shell(a):
    gap = floor(len(a)/2)
    while (gap > 0):
        for i in range(gap, len(a)):
            tmp, j = a[i], i
            while (j >= gap and a[j - gap] > tmp):
                a[j], j = a[j - gap], j - gap
            a[j] = tmp
        gap = floor(gap / 2)
