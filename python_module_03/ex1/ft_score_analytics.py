#!/usr/bin/env python3
import sys


def procces_score(argv) -> list:
    """Check if all the arguments is valid numbers"""
    scores = []
    argc = len(argv)
    if argc == 1:
        print("No scores provided. "
              "Usage: python3 ft_score_analytics.py <score1> <score2>...")
    else:
        error = False
        for i in range(1, argc):
            try:
                number = int(argv[i])
            except ValueError:
                error = True
                print("Error: All arguments must be valid integers")
                return None
            else:
                scores.append(number)
        if not error:
            print(f"Scores processed {scores}")
    return scores


def total_players(players: list) -> int:
    """Return the number of players"""
    return len(players)


def total_score(scores: list) -> int:
    """Return a sum of all the scores"""
    return sum(scores)


def average_score(scores: list) -> int:
    """Return the average of the scores"""
    i = len(scores)
    return total_score(scores) / i


def get_high_score(scores: list) -> int:
    """Return the highest score in the list"""
    return max(scores)


def get_low_score(scores: list) -> int:
    """Return the lowest score in the list"""
    return min(scores)


def score_range(scores: list) -> int:
    """Calculate the range of the scores"""
    return get_high_score(scores) - get_low_score(scores)


def ft_score_analytics():
    print("=== Player Score Analytics ===")

    players = procces_score(sys.argv)
    if players:
        print(f"Total players: {total_players(players)}")
        print(f"Total score: {total_score(players)}")
        print(f"Average score: {average_score(players)}")
        print(f"High score: {get_high_score(players)}")
        print(f"Low score: {get_low_score(players)}")
        print(f"Range score: {score_range(players)}")


# if __name__ == "__main__":
#     ft_score_analytics()
