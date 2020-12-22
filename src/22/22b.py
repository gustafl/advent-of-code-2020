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


def deja_vu(cards, previous_hands):
    fs = frozenset(cards)
    h = hash(fs)
    if h in previous_hands:
        return True


def play_game(p1_cards, p2_cards, game):
    p1_cards = p1_cards.copy()
    p2_cards = p2_cards.copy()
    p1_previous_hands = []
    p2_previous_hands = []
    print(f'== Game {game} ==\n')
    round_ = 1
    while p1_cards and p2_cards:
        # Make sure we haven't been here before in this game
        if deja_vu(p1_cards, p1_previous_hands) and deja_vu(p2_cards, p2_previous_hands):
            return 1  # Player 1 wins
        play_round(p1_cards, p2_cards, game, round_)
        round_ += 1


def play_round(p1_cards, p2_cards, game, round_):
    print(f'-- Round {round_} (Game {game}) --')
    print(f"Player 1's deck: {p1_cards}")
    print(f"Player 2's deck: {p2_cards}")
    p1_card = p1_cards.pop(0)
    print(f"Player 1 plays: {p1_card}")
    p2_card = p2_cards.pop(0)
    print(f"Player 2 plays: {p2_card}")
    if len(p1_cards) >= p1_card and len(p2_cards) >= p2_card:
        # Determine who wins the round by playing a new game of Recursive Combat
        pass
    else:
        # Determine who wins the round by comparing cards
        if p1_card > p2_card:
            print("Player 1 wins the round!\n")
            p1_cards.append(p1_card)
            p1_cards.append(p2_card)
        else:
            print("Player 2 wins the round!\n")
            p2_cards.append(p2_card)
            p2_cards.append(p1_card)


def calculate_score(cards):
    score = 0
    for i, v in enumerate(cards):
        score += v * (len(cards) - i)
    return score


def main():
    p1_cards, p2_cards = get_input('input.txt')
    game = 1
    while p1_cards and p2_cards:
        play_game(p1_cards, p2_cards, game)
        game += 1
    print("== Post-game results ==")
    print(f"Player 1's deck: {p1_cards}")
    print(f"Player 2's deck: {p2_cards}")
    cards = p1_cards if p1_cards else p2_cards
    score = calculate_score(cards)
    print(f"\nThe final score is: {score}")


main()
