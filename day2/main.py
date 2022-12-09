from day2.constants import SCORE_BY_PLAYS, PLAY_SCORES, X_Y_Z_SCORES, PLAY_TO_ACHIEVE_SCORE

if __name__ == '__main__':
    with open(f'data/challenge_input.txt') as f:
        lines = f.readlines()

        score_strategy_guide1 = 0
        score_strategy_guide2 = 0
        for line in lines:
            plays = line.strip().split(' ')
            opponent_play = plays[0]
            my_play = plays[1]

            score_strategy_guide1 += SCORE_BY_PLAYS[(opponent_play, my_play)] + PLAY_SCORES[my_play]

            required_score = X_Y_Z_SCORES[my_play]
            required_play = PLAY_TO_ACHIEVE_SCORE[(opponent_play, required_score)]

            score_strategy_guide2 += PLAY_SCORES[required_play] + required_score

    print("Score Part 1: ", score_strategy_guide1)
    print("Score Part 2: ", score_strategy_guide2)






