ticket = input('Enter the number of ticket you want to check (for example, "496417"): ')
unhappy = 100

def check_happy(ticket):
    return any(x for x in all_combinations(ticket) if x == unhappy)   # if True, the ticket is unhappy, because any
                                                                      # number in generator is equal unhappy (100)

def count_combs(ticket):
    # Return a number of founded unhappy numbers
    return len(list((x for x in all_combinations(ticket) if x == unhappy)))

def all_combinations(ticket):
    yield int(ticket)               # Numbers in the ticket became integers for operators
    for space in range(len(ticket) - 1):           # len(ticket) - 1 == number of spaces for operators
        for l in all_combinations(ticket[:space + 1]):   # left numbers from space
            for r in all_combinations(ticket[space + 1:]):   # right numbers from space
                # Set operators in space between left and right numbers
                yield l + r
                yield l - r
                yield l * r
                if r != 0: yield l / r        # DivisionByZero

def main(ticket):
    if ticket.isnumeric():
        if check_happy(ticket) is True:
            print("Your ticket is unhappy! "
                  "The unhappy number ({0}) was found {1} times!".format(unhappy, count_combs(ticket)))
        else:
            print("Your ticket is so happy, my friend!")
    else:
        ticket = input('Your ticket should consist of numbers, like "496417": ')
        main(ticket)
if __name__ == '__main__':
    main(ticket)
