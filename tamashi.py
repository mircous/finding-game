# https://www.practicepython.org/
def this_or_this(x):
    is_realy_greater = input('Is it greater tnan %s?'%x)
    if is_realy_greater == 'y':
        print('your number is %s'%(x+1))
    elif is_realy_greater == 'n':
        print('your number is %s'%x)

def guess():
    game_range = 1000
    zero = 0
    correct_answer = False

    while correct_answer is False:
        x = int((game_range + zero) / 2)
        first_part = range(zero, int(game_range/2))
        second_part = range(int(game_range/2),game_range)
        #print(first_part)
       # print(second_part)

        is_greater = input('Is it lower than %s?'%x)

        if is_greater == 'n':
            zero = x
            game_range + zero
            #x += int((game_range - x)/2)

            #zero = int((game_range - zero)/2)
        elif is_greater == 'y':
            game_range = x
            #game_range = int(game_range - game_range/2)
            #x = int(x/2)
        else:
            print('Wrong input')
        if game_range - zero == 1:
            #print('helllooooo')
            this_or_this(zero)
            break



guess()
