
helloworld = "Hello World"
directions = ['w-e', 'e-w', 'n-s', 's-n', 'nw-se', 'sw-ne', 'ne-sw', 'se-nw', 'hello']

direction = input("Choose a direction ({}) ".format(directions))

def hello_world(direction):
    if direction == 'w-e':
        print(helloworld)
    elif direction == 'e-w':
        wh = list(helloworld)
        wh.reverse()
        print(''.join(wh))
    elif direction == 'n-s':
        for ch in helloworld:
            print(ch)
    elif direction == 's-n':
        wh = list(helloworld)
        wh.reverse()
        for ch in wh:
            print(ch)
    elif direction == 'nw-se':
        for num, ch in enumerate(helloworld):
            print(' '*num, ch)
    elif direction == 'sw-ne':
        for num in range(len(helloworld), 0, -1):
            print(' ' * num, helloworld[num-1])
    elif direction == 'ne-sw':
        for num in range(len(helloworld), 0, -1):
            print(' ' * num, helloworld[len(helloworld) - num])
    elif direction == 'se-nw':
        wh = list(helloworld)
        wh.reverse()
        for num, ch in enumerate(wh):
            print(' ' * num, ch)
    elif direction == 'hello':
        for row in range(len(helloworld)):
            for column in range(len(helloworld) - row):
                print(" ", end="")
            for column in range(1, row + 1):
                print(helloworld[column-1], end="")
            for column in range(row - 1, 0, -1):
                print(helloworld[column-1], end="")
            print()

        for row in range(len(helloworld)):
            for column in range(row + 2):
                print(" ", end="")
            for column in range((len(helloworld)-2) - row):
                print(helloworld[column], end="")
            for column in range((len(helloworld)-3) - row, 0, -1):
                print(helloworld[column-1], end="")
            print()

def main(direction):
    if direction in directions:
        print('*'*20)
        hello_world(direction)
        print('*' * 20)
    else:
        direction = input("Please, input a correct direction ({})! ".format(directions))
        main(direction)

if __name__ == '__main__':
    main(direction)