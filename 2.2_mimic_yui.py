"""Імітація тексту

Прочитайте файл, вказаний в командній стрічці.
Використовуйте str.split() (без аргументів) для отримання всіх слів в файлі.
Замість того, щоб читати файл пострічково, простіше зчитати
його в одну велику стрічку і застосувати до неї split() один раз.

Створіть "імітаційний" словник, який зв’язує кожне слово
зі списком всіх слів, які безпосередньо слідують за цим словом в файлі.
Список слів може бути в довільному порядку і повинен включати дублікати. 

Так, наприклад, для тексту "Привіт, світ! Привіт, Всесвіт!" ми отримаємо такий
імітаційний словник:
{'': ['Привіт,'], 'Привіт,': ['світ!', 'Всесвіт!'], 'світ!': ['Привіт,']}
Будемо вважати, в якості ключа для першого слова в файлі використовується пуста
стрічка.

За допомогою імітаційного словника доволі просто генерувати випадкові тексти, 
які імітують оригінальний. Візьміть слово, перегляньте які слова можуть бути за ним, 
виберіть одне з них наугад, виведіть його і використовуйте це слово 
в наступній ітерації.

Використовуйте пусту стрічку в якості ключа для першого слова.
Якщо ви коли-небудь застрягнете на слові, якого немає в словнику,
повернітьсь до пустої стрічки, щоб продовжити генерацію тексту.

Стандартний python-модуль random включає в себе метод 
random.choice(list), який вибирає випадковий елемент із непустого списку.

"""

import random
import sys


def mimic_dict(filename):
    """Повертає імітаційний словник, який співставляє кожне слово 
    зі списком слів, які безпосередньо слідують за ним в тексті"""
    # +++ваш код+++
    f = open(filename, "r", encoding='utf-8') # для запуску з командної строки Windows використовував 'cp866'
    text = f.read()          
    words = text.split() 
    word_dict = {' ': words[0], }   # словник із першим елементом
    count = 0
    for word in words:
        # Даний блок просто додає ключі (якщо їх немає) і присвоює їм значення
        if words.index(word) < (len(words)-1) and word not in word_dict:
            word_dict[word] = word_dict.setdefault(word, words[count+1])
            count+=1
        # Даний блок додає значення до ключа, якщо ключ уже існує
        elif word in word_dict:
            # Забирає значення із ключа
            value =  word_dict.setdefault(word, None)
            # Якщо значення є стрічкою, то перетворює її в список, якщо вона уже є списком, то просто пропускає
            if type(value) == str:
                value_l = value.split()
            else:
                value_l = value
            value_l.append(words[count+1])   #Додає значення до списку 
            word_dict[word] = value_l        #Присвоєю список(59) як значення для ключа в словнику
            count+=1
    return word_dict
    f.close()


def print_mimic(mimic_dict, word):
    """Приймає в якості аргументів імітаційний словник і початкове слово,
    виводить 200 випадкових слів, згідно правил імітації."""
    # +++ваш код+++
    count = 0
    while count<200:
        # Цей блок відповідає за виведення слова
        if type(word) == type([]):     #word == list
            word = random.choice(word) 
            print(word)
            count+=1
        else:
            print(word)
            count+=1
        # Цей блок відповідає за рух по словнику згідно правил імітації
        if word in mimic_dict:
            word = mimic_dict[word]
        else:
            word = mimic_dict[' ']

def main():
    if len(sys.argv) != 2:
        print('usage: ./mimic.py file-to-read')
        sys.exit(1)

    d = mimic_dict(sys.argv[1])
    print_mimic(d, '')


if __name__ == '__main__':
    main()
