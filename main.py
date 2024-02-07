# Let's correct the logic in the provided script and test it directly here to ensure it works as expected.

from itertools import combinations, product

class Card:
    ranks = '23456789TJQKA'
    suits = 'shdc'
    rank_values = {rank: i+2 for i, rank in enumerate(ranks)}
    str_to_rank = {rank: i+2 for i, rank in enumerate(ranks)}
    rank_to_str = {i+2: rank for i, rank in enumerate(ranks)}

    def __init__(self, rep):
        self.rank = self.str_to_rank[rep[0]]
        self.suit = rep[1]
        self.value = self.rank_values[rep[0]]

    def __repr__(self):
        return f"{self.rank_to_str[self.rank]}{self.suit}"

def calculate_hand_score(hand_str):
    hand = [Card(hand_str[i:i+2]) for i in range(0, 10, 2)]
    ranks = [card.rank for card in hand]
    suits = [card.suit for card in hand]
    rank_counts = {rank: ranks.count(rank) for rank in set(ranks)}
    is_flush = len(set(suits)) == 1
    sorted_ranks = sorted(ranks, reverse=True)
    is_straight = sorted_ranks in [list(range(sorted_ranks[0], sorted_ranks[0] - 5, -1)), [14, 5, 4, 3, 2]]
    sorted_rank_counts = sorted(rank_counts.values(), reverse=True)
    main_cards_score = 0
    aux_cards_score = 0

    # Calculate main and auxiliary card scores separately
    for rank, count in rank_counts.items():
        if count == max(sorted_rank_counts):
            main_cards_score += rank * count
        else:
            aux_cards_score += rank * count

    if is_straight and is_flush:
        category = "Straight Flush"
        score = 10**7 + main_cards_score
    elif sorted_rank_counts[0] == 4:
        category = "Four of a Kind"
        score = 10**6 + main_cards_score * 10 + aux_cards_score
    elif sorted_rank_counts == [3, 2]:
        category = "Full House"
        score = 10**5 + main_cards_score * 10 + aux_cards_score
    elif is_flush:
        category = "Flush"
        score = 10**4 + sum(sorted_ranks)
    elif is_straight:
        category = "Straight"
        score = 10**3 + sum(sorted_ranks)
    elif sorted_rank_counts[0] == 3:
        category = "Three of a Kind"
        score = 10**2 + main_cards_score * 10 + aux_cards_score
    elif sorted_rank_counts == [2, 2, 1]:
        category = "Two Pair"
        score = 10**1 + main_cards_score * 10 + aux_cards_score
    elif sorted_rank_counts[0] == 2:
        category = "One Pair"
        score = main_cards_score * 10 + aux_cards_score
    else:
        category = "High Card"
        score = sum(sorted_ranks)

    return category, score

# Testing the function with a variety of hands
test_hands = ["KcKdAsTc2c", "KcKdAsTc5s", "QdQcAsTc5c", "AsAhKcKdTc", "7s7d7c5d5c", "7s7d7c6s6c","8c8d8hAcKc","9c9d9h2d3d","2c3c4c5c6c","2c3c4c5c7c","2c3c4c5c8c","2c3c4c5c9c","2c3c4c5cTc","2c3c4c5cJc","2c3c4c5cQc","2c3c4c5cKc","2c3c4c5cAc","2c3c4c5c6c","2c3c4c5c7c","2c3c4c5c8c","2c3c4c5c9c","2c3c4c5cTc","2c3c4c5cJc","2c3c4c5cQc","2c3c4c5cKc","2c3c4c5cAc","2c3c4c5c6c","2c3c4c5c7c","2c3c4c5c8c","2c3c4c5c9c","2c3c4c5cTc","2c3c4c5cJc","2c3c4c5cQc","2c3c4c5cKc","2c3c4c5cAc","2c3c4c5c6c","2c3c4c5c7c","2c3c4c5c8c","2c3c4c5c9c","2c3c4c5cTc","2c3c4c5cJc","2c3c4c5cQc","2c3c4c5cKc","2c3c4c5cAc"]

# generate random 5 card combos
for hand in test_hands:
    print(hand, calculate_hand_score(hand))