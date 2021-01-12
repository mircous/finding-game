
def guess():
    game_range = 1000
    zero = 0
    correct_answer = False
    while correct_answer is False:
        first_part = range(zero, int(game_range/2))
        second_part = range(int(game_range/2),game_range)

        is_greater = input('Is it greater than %s?'%(game_range/2))
        
        if is_greater == 'y':
            zero = (game_range - zero)/2
        elif is_greater == 'n':
            game_range = game_range - game_range/2
        else:
            print('Wrong input')

guess()
