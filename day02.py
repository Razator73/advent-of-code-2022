opponent = {'A': 'rock', 'B': 'paper', 'C': 'scissors'}
player = {'X': 'rock', 'Y': 'paper', 'Z': 'scissors'}
score = {'rock': 1, 'paper': 2, 'scissors': 3}
beats = {'rock': 'scissors', 'paper': 'rock', 'scissors': 'paper'}
loses_to = {'rock': 'paper', 'paper': 'scissors', 'scissors': 'rock'}

# test_input = 'A Y\nB X\nC Z'
# games = test_input.split('\n')
with open('input/day2.txt') as f:
    games = [game for game in f.read().split('\n') if game]

# Part 1
game_scores = {}
for game in set(games):
    opp_play, player_play = game.split(' ')
    game_score = score[player[player_play]]
    if beats[player[player_play]] == opponent[opp_play]:
        game_score += 6
    elif player[player_play] == opponent[opp_play]:
        game_score += 3
    game_scores[game] = game_score

total_score = 0
for game in games:
    total_score += game_scores[game]
print(total_score)

# Part 2
total_score = 0
for game in games:
    opp_play, result = game.split(' ')
    if result == 'X':
        total_score += score[beats[opponent[opp_play]]]
    elif result == 'Y':
        total_score += 3 + score[opponent[opp_play]]
    elif result == 'Z':
        total_score += score[loses_to[opponent[opp_play]]] + 6
print(total_score)
