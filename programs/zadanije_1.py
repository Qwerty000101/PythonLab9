#!/usr/bin/env python3
# -*- coding: utf-8 -*-


if __name__ == '__main__':
    school = {"1а": 20, "1б": 30, "1в": 40}
    print(school)
    #Изменение количества учащихся в одном из классов
    school["1а"] = 10
    print(school)

    #Создание нового класса
    school["1г"] = 50
    print(school)

    #Расформирование класса
    school.pop("1а")
    print(school)

    counter = 0
    for i in school.keys():
        counter += school[i]
    
    print(f"Всего учащихся в школе: {counter}")