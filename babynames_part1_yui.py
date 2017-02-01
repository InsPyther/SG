#!/usr/bin/python3



"""Завдання "Детячі імена"

РАГС веде статистику детячих імен. На сайті цієї організації 
публікується статистика найбільш популярних імен за роком народження дитини.

Файли для цього завдання знаходяться в файлах "babynames_boys.html" і 
"babynames_girls.html". Вони містять сирий HTML-код.

Гляньте на HTML і подумайте про те, як ви можете отримати дані з нього
за допомогою регулярних виразів.

-= 1 частина =-

1. Створити функцію extract_names(filename), яка приймає в якості 
аргумента ім’я файлу і повертає дані з нього в виді словника виду:
babynames = {
'Софія': ['3841 (6,0%)*', '3668 (6,2%)', '2127 (4,8%)', 
    '826 (2,4%)', '193 (0,4%)',],
'Вікторія': ['2219', '1994', '1829', '1076', '1033'],
...
}
Словник використовує в якості ключа ім’я дитини, а в якості значення -
список, що містить кількість дітей, названих цим іменем у відповідному році.  
Для спрощення задачі використовуйте стрічки в тому виді, в якому вони містяться 
в HTML-файлі.

2. Створіть функцію print_names(). Функція отримує в якості аргумента 
словник babynames з даними виду ключ/список (опис словника вище). 

Потім:

1. Запитує у користувача рік, який його цікавить (бажано вивести список 
    можливих варіантів і попросити ввести дані заново, якщо за вказаним 
    роком немає даних).

2. Виводить на друк дані в алфавітному порядку імен:
    Аліна 837
    Аліса 1239
    Олена 658
    ...

Підказка: створіть службовий список з роками народження: 
years = ['2012', '2010',...].
З його допомогою вам буде простіше визначати позицію даних за роком в списку 
словника babynames.

Порада: зручніше за все писати програму, розділивши її на серію невеликих етапів,
виводячи на друк результати кожного кроку. 


-= 2 частина =-

1. Ускладніть функцію extract_names(filename). Нехай тепер вона повертає 
словник виду:
babynames = {
    'Софія': {
        2012: [3841, 6.0]', 
        2010: [3668, 6.2]',
        2005: [2127, 4.8]',
        2000: [826, 2.4]',
        1990: [193, 0.4]',
    },
    'Вікторія': {
        2012: [2219, None],
        2010: [1994, None],
        2005: [1829, None],
        2000: [1076, None],
        1990: [1033, None],
    },
    ...
}
Словник використовує в якості ключа ім’я дитини, а в якості значення -
ще один словник, який містить список, перший елемент якого містить 
кількість дітей, а другий - дані в процентах, отримані з файлу
(None, якщо поле таблиці в файлі не містить процентних даних).

2. Функція print_names() працює аналогічним чином, але видача сортується
тепер за кількістю дітей і форматується наступним чином:

Софія    3841   6,0%
Марія    3735   5,8%
...
Вікторія 2219
...

3. Нехай функція print_names() тепер запитує дані в циклі,
щоб дати користувачу можливість отримати вибірку за різні роки.
В кінці кожної ітерації запитувати користувача, чи хоче він продовжити роботу:
Продовжити? (y/n)
Якщо введено 'n' - вийдіть з програми.
"""

import re
import os
import sys
from bs4 import BeautifulSoup

def extract_names(filename):
    """
    Отримує ім’я файлу. 
    Повертає дані з файлу в виді словника:
    {
    'Софія': ['3841 (6,0%)*', '3668 (6,2%)', '2127 (4,8%)', 
        '826 (2,4%)', '193 (0,4%)',],
    'Вікторія': ['2219', '1994', '1829', '1076', '1033'],
    ...
    }
    """
    html = open(filename, "r+", encoding='utf-8').read()
    table = BeautifulSoup(html, "html.parser")
    tags = table.find_all('tr')

    tabledict = {}

    for tag in tags:

        dictkey = re.findall('<td width="[175]{3}">\s+([\S]*)\s+</td>',tag.decode())    #імена
        dictvalue = re.findall('<td width="7?6?[90]*?[104]*?[94]*?[85]*?">\s*([0-9].{1,})\s*</td>',tag.decode()) #кількість (список)
        
        if dictkey!= [] and dictvalue != []:   # відсів порожніх значень (заголовків для стовпців)
            tabledict[dictkey[0]] = dictvalue

    return tabledict



def print_names(babynames):
    # +++ваш код+++
    years = ['2012', '2010', '2005', '2000', '1990']
    year = input('Please, choose an year {} : '.format(years))

    while True:
        if year in years:
            # сортування словника
            dict_keys = babynames.keys()
            key_list = list(dict_keys)
            key_list.sort()
            # друк словника
            for key in key_list:
                print(key, babynames[key][years.index(year)])
            break
        else:
            # повтор, на випадок неправильного вводу
            year = input("You are choosed a wrong year. Please choose one of {}: ".format(years))

def main():
    # Код розбору командної стрічки
    # Отримаємо список аргументів командної стрічки, відкинувши [0] елемент, 
    # який містить ім’я скрипта
    args = sys.argv[1:]

    if not args:
        print('usage: filename')
        sys.exit(1)

    filename = args[0]
    babynames = extract_names(filename)
    print_names(babynames)

  
if __name__ == '__main__':
    main()