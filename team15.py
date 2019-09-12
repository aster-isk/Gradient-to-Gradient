import random


team_name = 'Ghost' # Only 10 chars displayed.
strategy_name = 'Point Ratio'
strategy_description = 'keeps track of points won or lost by computers choice and chooses acccordinly by comparing the ratios of b and c, first selection is random'
    
def move(my_history, their_history, my_score, their_score):
    random_char = ['c', 'b']
    if len(my_history) == 0:
        return(random.choice(random_char))
    else:
        c_count = 0
        b_count = 0
        turns_played = len(my_history)
        if my_history[:-1] == 'c':
            if their_history[:-1] == 'c':
                c_count += 0
        if my_history[:-1] == 'b':
            if their_history[:-1] == 'c':
                b_count += 10
        if my_history[:-1] == 'c':
            if their_history[:-1] == 'b':
                c_count -= 50
        if my_history[:-1] == 'b':
            if their_history[:-1] == 'b':
                b_count -= 25
        c_percent = c_count / turns_played
        b_percent = b_count / turns_played
        if b_percent >= c_percent:
            return 'b'
        else:
            return 'c'
    # my_history: a string with one letter (c or b) per round that has been played with this opponent.
    # their_history: a string of the same length as history, possibly empty. 
    # The first round between these two players is my_history[0] and their_history[0].
    # The most recent round is my_history[-1] and their_history[-1].
    
    # Analyze my_history and their_history and/or my_score and their_score.
    # Decide whether to return 'c' or 'b'.
    
    
def test_move(my_history, their_history, my_score, their_score, result):
    '''calls move(my_history, their_history, my_score, their_score)
    from this module. Prints error if return value != result.
    Returns True or False, dpending on whether result was as expected.
    '''
    real_result = move(my_history, their_history, my_score, their_score)
    if real_result == result:
        return True
    else:
        print("move(" +
            ", ".join(["'"+my_history+"'", "'"+their_history+"'",
                       str(my_score), str(their_score)])+
            ") returned " + "'" + real_result + "'" +
            " and should have returned '" + result + "'")
        return False
