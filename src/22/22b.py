def get_input(file):
    with open(file, 'rt', encoding='utf8') as f:
        lines = [line.strip() for line in f]

    p1_cars = get_player_cards(lines, 1)
    p2_cars = get_player_cards(lines, 2)
    return p1_cars, p2_cars


def get_player_cards(lines, player):
    start = lines.index(f'Player {player}:') + 1
    end = lines.index('')
    if end < start:
        end = len(lines)
    cards = lines[start:end]
    cards = list(map(lambda x: int(x), cards))
    return cards


def hand_to_hash(hand):
    s = " ".join(str(x) for x in hand)
    h = hash(s)
    return h


def deja_vu(hand, previous_hands):
    hand = hand_to_hash(hand)
    if hand in previous_hands:
        return True
    else:
        return False


def play_game(p1_hand, p2_hand, game):
    p1_previous_hands = []
    p2_previous_hands = []
    print(f'\n== Game {game} ==\n')
    round_ = 1
    while p1_hand and p2_hand:
        # Make sure we haven't been here before in this game
        if deja_vu(p1_hand, p1_previous_hands) and \
           deja_vu(p2_hand, p2_previous_hands):
            return 1  # Player 1 wins
        else:
            # If this is a new situation in this game,
            # save the new hands
            p1_previous_hands.append(hand_to_hash(p1_hand))
            p2_previous_hands.append(hand_to_hash(p2_hand))
            # Play new round
            p1_hand, p2_hand = play_round(p1_hand, p2_hand, game, round_)

        if p1_hand and not p2_hand:
            print(f"Player 1 wins game {game}!\n")
            return 1

        if p2_hand and not p1_hand:
            print(f"Player 2 wins game {game}!\n")
            return 2

        round_ += 1


def play_round(p1_hand, p2_hand, game, round_):
    print(f'-- Round {round_} (Game {game}) --')
    print(f"Player 1's deck: {p1_hand}")
    print(f"Player 2's deck: {p2_hand}")
    p1_card = p1_hand.pop(0)
    print(f"Player 1 plays: {p1_card}")
    p2_card = p2_hand.pop(0)
    print(f"Player 2 plays: {p2_card}")
    # If both players have at least as many cards in their own decks as
    # the number on the card they just dealt
    if len(p1_hand) >= p1_card and len(p2_hand) >= p2_card:
        # The winner of the round is determined by recursing into a
        # sub-game of Recursive Combat
        p1_hand_copy = p1_hand[:p1_card].copy()
        p2_hand_copy = p2_hand[:p2_card].copy()
        winner = play_game(p1_hand_copy, p2_hand_copy, game + 1)
        if winner == 1:
            p1_hand.append(p1_card)
            p1_hand.append(p2_card)
        else:
            p2_hand.append(p2_card)
            p2_hand.append(p1_card)
    else:
        # Determine who wins the round by comparing cards
        if p1_card > p2_card:
            print(f"Player 1 wins round {round_} of game {game}!\n")
            p1_hand.append(p1_card)
            p1_hand.append(p2_card)
        else:
            print(f"Player 2 wins round {round_} of game {game}!\n")
            p2_hand.append(p2_card)
            p2_hand.append(p1_card)

    return p1_hand, p2_hand


def calculate_score(hand):
    score = 0
    for i, v in enumerate(hand):
        score += v * (len(hand) - i)
    return score


def main():
    p1_hand, p2_hand = get_input('input.txt')
    game = 1
    while p1_hand and p2_hand:
        play_game(p1_hand, p2_hand, game)
        game += 1
    print("== Post-game results ==")
    print(f"Player 1's deck: {p1_hand}")
    print(f"Player 2's deck: {p2_hand}")
    hand = p1_hand if p1_hand else p2_hand
    score = calculate_score(hand)
    print(f"\nThe final score is: {score}")


main()

# This gives the correct outputs (291 on sample.txt, 35070 on
# input.txt), but it takes several minutes to compute, and the 'game'
# variable doesn't update properly.
#
# TODO: Make the 'game' variable global.
# TODO: Try to speed it up after studying how to combine recursion with concurrency.
