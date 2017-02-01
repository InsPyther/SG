from random import choice

name = input("What is your name? ")

def hello(name):
    name = name.capitalize()
    hellovariants = ["Hello", "Greetings", "Hola", "Hi"]
    print('{0}, {1}!'.format(choice(hellovariants), name))

def main(name):
    if name.isalpha():
        hello(name)
    else:
        name = input("Please, input a correct name! ")
        main(name)

if __name__ == '__main__':
    main(name)
