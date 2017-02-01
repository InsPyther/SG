horses = input("How much horses are you want to test? ")

def find_fastest(num, newnum=0, race=0):
    while num > 3:        # Four and more
        num -= 5          # -5 horses are equal to +1 race
        race += 1
        newnum += 3       # Gets 3 fastest from the race
    else:
        newnum += num               # If we have 3 or less horses after while cycle they are added to the next func call
        if newnum > 3:              # If we don't found 3 fastest horses after while cycle: call the func one more time
            find_fastest(newnum, race=race)      # Gets newnum as num and race from the while cycle
        else:
            print(race)         # If we find 3 fastest horses: print the number of races


def main(horses):
    if horses.isnumeric():
        print('-'*30,'\nThe minimum number of races is:')
        find_fastest(int(horses))
    else:
        horses = input("Please, input a number of whole horses for testing! ")
        main(horses)

if __name__ == '__main__':
    main(horses)

