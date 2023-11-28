#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def generate_subsets(n, t=[]):
    if n == 0:
        print(t)
        return
    generate_subsets(n - 1, t + [n])
    generate_subsets(n - 1, t)

if __name__ == '__main__':
    n = int(input("Введите значения n: "))
    generate_subsets(n)
