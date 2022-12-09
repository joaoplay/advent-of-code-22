PLAY_SCORES = {
    'X': 1,
    'Y': 2,
    'Z': 3,
}

WIN_SCORE = 6
LOOSE_SCORE = 0
DRAW_SCORE = 3

X_Y_Z_SCORES = {
    'X': LOOSE_SCORE,
    'Y': DRAW_SCORE,
    'Z': WIN_SCORE,
}

SCORE_BY_PLAYS = {
    ('A', 'X'): 3,
    ('B', 'Y'): 3,
    ('C', 'Z'): 3,
    ('A', 'Y'): 6,
    ('A', 'Z'): 0,
    ('B', 'X'): 0,
    ('B', 'Z'): 6,
    ('C', 'X'): 6,
    ('C', 'Y'): 0,
}

PLAY_TO_ACHIEVE_SCORE = {(plays[0], score): plays[1] for plays, score in SCORE_BY_PLAYS.items()}
