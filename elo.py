""" The first step is to compute the transformed rating for each player or team:

R(1) = 10^R(1)/400

R(2) = 10^R(2)/400 

 In the second step we calculate the expected score for each player:

E(1) = R(1) / (R(1) + R(2))

E(2) = R(2) / (R(1) + R(2))

set the actual score in the third step:

S(1) = 1 if player 1 wins / 0.5 if draw / 0 if player 2 wins

S(2) = 0 if player 1 wins / 0.5 if draw / 1 if player 2 wins

Now we can put it all together and in a fourth step find out the updated Elo-rating for each player:

r'(1) = r(1) + K * (S(1) – E(1))

r'(2) = r(2) + K * (S(2) – E(2))

"""
#maybe try an alternative calculation algorithm

class chessPlayer:
    def __init__(self, elo, win):
        self.elo = elo
        self.win = win

def compute_transformed_rating(elo):
    transformed = 10.0**(elo/400.0)
    return transformed

#find a more elegant way for the dividend
def calculate_expected_score(elo1, elo2):
    expected = elo1 / (elo1 + elo2)
    return expected

def calculate_new_elo(win1, win2, elo1, elo2, exp1, exp2, K):
    if win1:
        score1 = 1.0
        score2 = 0.0
    elif win2:
        score1 = 0.0
        score2 = 1.0
    else:
        score1 = 0.5
        score2 = 0.5

    new_elo1 = elo1 + K * (elo1 - exp1)
    new_elo2 = elo2 + K * (elo2 - exp2)

    return new_elo1, new_elo2

def main():
    K = 32
    player_one = chessPlayer(1000, win=True)
    player_two = chessPlayer(1400, win=False)

    player_one_transformed = compute_transformed_rating(player_one.elo)
    player_two_transformed = compute_transformed_rating(player_two.elo)
    new_one, new_two = calculate_new_elo(
        player_one.win,
        player_two.win,
        player_one_transformed,
        player_two_transformed,
        calculate_expected_score(player_one.elo, player_two.elo,),
        calculate_expected_score(player_two.elo, player_one.elo,),
        K,
    )

    print(f"old elo\nPlayer One: {player_one.elo},\tPlayer Two: {player_two.elo}\n\nNew elo\nPlayer One: {new_one}\tPlayer Two:{new_two}")

main()

