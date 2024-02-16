#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == "__main__":

    letters = {'а', 'о', 'у', 'э', 'ы', 'я', 'ё', 'е', 'ю', 'и'}

    string = input("Введите строку (на русском): ")

    count = sum(1 for char in string.lower() if char in letters)

    print(f"Количество гласных в введенной строке: {count}")
