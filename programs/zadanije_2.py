#!/usr/bin/env python3
# -*- coding: utf-8 -*-


if __name__ == '__main__':
    d = {1: "a", 2: "b", 3: "c"}
    print(d)
    swapped = {v: k for k, v in d.items()}
    print(swapped)