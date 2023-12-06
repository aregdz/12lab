#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time
import random

def count_inversions(arr):
    if len(arr) <= 1:
        return arr, 0

    mid = len(arr) // 2
    left, inv_left = count_inversions(arr[:mid])
    right, inv_right = count_inversions(arr[mid:])

    merged, inv_merge = merge_and_count(left, right)

    return merged, (inv_left + inv_right + inv_merge)

def merge_and_count(left, right):
    merged = []
    inv_count = 0
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            inv_count += len(left) - i
            j += 1

    merged.extend(left[i:])
    merged.extend(right[j:])

    return merged, inv_count

if __name__ == '__main__':
    arr = [random.randint(1, 100) for i in range(1000)]
    print(len(arr))
    start_time = time.time()
    sorted_arr, inversions = count_inversions(arr)
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Исходный массив: {arr}")
    print(f"Отсортированный массив: {sorted_arr}")
    print(f"Количество инверсий: {inversions}")
    print(f"Время выполнения: {elapsed_time*1000} милисекунд")