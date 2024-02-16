#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == "__main__":

    all = {'a', 'b', 'g', 'h', 'j', 'k', 'l', 'o', 'p', 'q', 'r', 's', 'u', 'v', 'z'}
    A = {'a', 'b', 'h', 'k', 'o', 'r'}
    B = {'b', 'g', 'h', 'l', 's'}
    C = {'k', 'l', 'z'}
    D = {'g', 'j', 'p', 'q', 'u', 'v'}

    X = (A | B) & D
    Y = (all - A) & (all - B) - (C | D)

    print("Результат X:", X)
    print("Результат Y:", Y)
    