#
'''
1. Написати просту програму для імітації роботи команди  Unix - grep.
(Програма командного рядка, вбудована в Unix називається grep
(Generalized Regular Expression Parser), що робить майже таке саме,
як приклади з search().)

Попросіть користувача ввести регулярний вираз і підрахувати кількість рядків,
які відповідають регулярному виразу:
$ python grep.py
Enter a regular expression: ^Author
mbox.txt had 1798 lines that matched ^Author

$ python grep.py
Enter a regular expression: ^X-
mbox.txt had 14368 lines that matched ^X-

$ python grep.py
Enter a regular expression: java$
mbox.txt had 4218 lines that matched java$'''

import re

file_name ='mbox-short.txt'                #виділив у змінну, щоб, при потребі, через input присвоювати значення
file = open(file_name)

reg = str(input('Input a regular expression: '))
i = 0
for line in file:
    line = line.rstrip()
    x = re.search(reg, line)
    if not x:
        continue
    i+=1
print(('{} had {} lines that matched {}').format(file_name, i, reg))

'''
2. Написати програму для пошуку рядків виду
"New Revision: 39772"
і витягти число з кожної з стрічок, використовуючи регулярний вираз
і метод findall().
Обчислити середнє значення чисел і роздрукувати середнє значення.

Enter file:mbox.txt
38549.7949721

Enter file:mbox-short.txt
39756.9259259
'''
name_file = str(input('Enter file: '))
f = open(name_file)
pattern = 'New Revision: ([0-9]+)'           # паттерн повертає тільки групу цифр
lst = []
for line in f:
    line = line.rstrip()
    x = re.findall(pattern, line)
    if not x:
        continue
    lst.extend(x)

print(sum(map(int, lst))/len(lst))           #використав функц. програмування
