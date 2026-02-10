#!/usr/bin/env python3

def list_comprehension(data: dict) -> None:
    """List Comprehension Examples"""
    print("\n=== List Comprehension Examples ===")

    high_plyrs = [name
                  for name, info in data.items()
                  if info.get('total_score') > 2000]
    print(f"High scorers (>2000): {high_plyrs}")

    high_scores = [scr.get('total_score')*2
                   for scr in data.values()
                   if scr.get('total_score') > 2000]
    print(f"Scores doubled: {high_scores}")

    on_plyrs = [name
                for name, info in data.items()
                if info.get('online')]
    print(f"Active players: {on_plyrs}")


def dict_comprehension(data: dict) -> None:
    """dict Comprehension Examples"""
    print("\n=== Dict Comprehension Examples")

    plyrs_scr = {name: info.get('total_score')
                 for name, info in data.items()}
    print(f"Player scores: {plyrs_scr}")

    modes = ['casual', 'competitive', 'ranked']
    game_modes = {name: len(modes) - modes.index(name)
                  for name in modes}
    print(f"Game modes: {game_modes}")

    plyrs_ach = {name: info.get('achievements_count')
                 for name, info in data.items()}
    print(f"Achievement count: {plyrs_ach}")


def set_comprehension(sessions: dict) -> None:
    """set Comprehension Examples"""
    print("\n=== Set Comprehension Examples ===")

    plyrs = {name.get('player')
             for name in sessions}
    print(f"Unique players: {plyrs}")

    rkd_plyrs = {name.get('player')
                 for name in sessions
                 if name.get('mode') == 'ranked' and
                 name.get('completed')}
    print(f"Players completed a ranked {rkd_plyrs}")

    short_session = {name.get('player')
                     for name in sessions
                     if name.get('duration_minutes') < 30}
    print(f"Short session (<30\") {short_session}")


def total_players(data: dict) -> int:
    """
    Get the total number of players in the dataset.

    :param data: Dictionary where keys represent player names.
    :return: The total count of unique players.
    """
    total_plyrs = [player
                   for player in data.keys()]
    return len(total_plyrs)


def modes_played(data: dict) -> set:
    """
    Extract all unique game modes present in the data.

    :param data: A list of dictionaries, where each dict contains a 'mode' key.
    :return: A set of unique strings representing the game modes played.
    """
    modes = {mode.get('mode')
             for mode in data}
    return modes


def average_session_duration(data: dict) -> float:
    """
    Calculate the average duration of game sessions.

    :param data: A list of dictionaries, each containing a
                'duration_minutes' key.
    :return: The mean duration as a float.
    """
    durations = [time.get('duration_minutes')
                 for time in data]
    return sum(durations) / len(durations)


def top_player(data: dict) -> dict:
    """
    Find the player or players with the highest total score.

    :param data: Dictionary where keys are player names and values are dicts
                 with 'total_score'.
    :return: A dictionary containing the top player(s) and their information.
    """
    scores = [info.get('total_score')
              for name, info in data.items()]
    max_score = max(scores)
    top_player = {name: info
                  for name, info in data.items()
                  if info.get('total_score') == max_score}
    return top_player


def main():
    print("=== Game Analytics Dashboard ===")

    players = {'alice': {'level': 41,
                         'total_score': 2824,
                         'sessions_played': 13,
                         'favorite_mode': 'ranked',
                         'achievements_count': 5,
                         'online': True},
               'bob': {'level': 16,
                       'total_score': 4657,
                       'sessions_played': 27,
                       'favorite_mode': 'ranked',
                       'achievements_count': 2,
                       'online': True},
               'charlie': {'level': 44,
                           'total_score': 9935,
                           'sessions_played': 21,
                           'favorite_mode': 'ranked',
                           'achievements_count': 7,
                           'online': True},
               'diana': {'level': 3,
                         'total_score': 1488,
                         'sessions_played': 21,
                         'favorite_mode': 'casual',
                         'achievements_count': 4,
                         'online': False},
               'eve': {'level': 33,
                       'total_score': 1434,
                       'sessions_played': 81,
                       'favorite_mode': 'casual',
                       'achievements_count': 7,
                       'online': False},
               'frank': {'level': 15,
                         'total_score': 8359,
                         'sessions_played': 85,
                         'favorite_mode': 'competitive',
                         'achievements_count': 1,
                         'online': False}}

    sessions = [
        {'player': 'bob',
         'duration_minutes': 94,
         'score': 1831,
         'mode': 'competitive',
         'completed': False},
        {'player': 'bob',
         'duration_minutes': 32,
         'score': 1478,
         'mode': 'casual',
         'completed': True},
        {'player': 'diana',
         'duration_minutes': 17,
         'score': 1570,
         'mode': 'competitive',
         'completed': False},
        {'player': 'alice',
         'duration_minutes': 98,
         'score': 1981,
         'mode': 'ranked',
         'completed': True},
        {'player': 'diana',
         'duration_minutes': 15,
         'score': 2361,
         'mode': 'competitive',
         'completed': False},
        {'player': 'eve',
         'duration_minutes': 29,
         'score': 2985,
         'mode': 'casual',
         'completed': True},
        {'player': 'frank',
         'duration_minutes': 34,
         'score': 1285,
         'mode': 'casual',
         'completed': True},
        {'player': 'alice',
         'duration_minutes': 53,
         'score': 1238,
         'mode': 'competitive',
         'completed': False},
        {'player': 'bob',
         'duration_minutes': 52,
         'score': 1555,
         'mode': 'casual',
         'completed': False},
        {'player': 'frank',
         'duration_minutes': 92,
         'score': 2754,
         'mode': 'casual',
         'completed': True},
        {'player': 'eve',
         'duration_minutes': 98,
         'score': 1102,
         'mode': 'casual',
         'completed': False},
        {'player': 'diana',
         'duration_minutes': 39,
         'score': 2721,
         'mode': 'ranked',
         'completed': True},
        {'player': 'frank',
         'duration_minutes': 46,
         'score': 329,
         'mode': 'casual',
         'completed': True},
        {'player': 'charlie',
         'duration_minutes': 56,
         'score': 1196,
         'mode': 'casual',
         'completed': True},
        {'player': 'eve',
         'duration_minutes': 117,
         'score': 1388,
         'mode': 'casual',
         'completed': False},
        {'player': 'diana',
         'duration_minutes': 118,
         'score': 2733,
         'mode': 'competitive',
         'completed': True},
        {'player': 'charlie',
         'duration_minutes': 22,
         'score': 1110,
         'mode': 'ranked',
         'completed': False},
        {'player': 'frank',
         'duration_minutes': 79,
         'score': 1854,
         'mode': 'ranked',
         'completed': False},
        {'player': 'charlie',
         'duration_minutes': 33,
         'score': 666,
         'mode': 'ranked',
         'completed': False},
        {'player': 'alice',
         'duration_minutes': 101,
         'score': 292,
         'mode': 'casual',
         'completed': True},
        {'player': 'frank',
         'duration_minutes': 25,
         'score': 2887,
         'mode': 'competitive',
         'completed': True},
        {'player': 'diana',
         'duration_minutes': 53,
         'score': 2540,
         'mode': 'competitive',
         'completed': False},
        {'player': 'eve',
         'duration_minutes': 115,
         'score': 147,
         'mode': 'ranked',
         'completed': True},
        {'player': 'frank',
         'duration_minutes': 118,
         'score': 2299,
         'mode': 'competitive',
         'completed': False},
        {'player': 'alice',
         'duration_minutes': 42,
         'score': 1880,
         'mode': 'casual',
         'completed': False},
        {'player': 'alice',
         'duration_minutes': 97,
         'score': 1178,
         'mode': 'ranked',
         'completed': True},
        {'player': 'eve',
         'duration_minutes': 18,
         'score': 2661,
         'mode': 'competitive',
         'completed': True},
        {'player': 'bob',
         'duration_minutes': 52,
         'score': 761,
         'mode': 'ranked',
         'completed': True},
        {'player': 'eve',
         'duration_minutes': 46,
         'score': 2101,
         'mode': 'casual',
         'completed': True},
        {'player': 'charlie',
         'duration_minutes': 117,
         'score': 1359,
         'mode': 'casual',
         'completed': True}]

    list_comprehension(players)
    dict_comprehension(players)
    set_comprehension(sessions)

    print("\n=== Combined Analysis ===")

    print(f"Total Players: {total_players(players)}")
    print(f"Game modes played: {modes_played(sessions)}")

    print("Average session duration (minutes): "
          f"{average_session_duration(sessions)}\"")

    plyr = top_player(players)
    [(name, info)] = plyr.items()
    print(f"Top Player: {name} ({info.get('total_score')} points, "
          f"{info.get('achievements_count')} achievements)")


# if __name__ == "__main__":
#     main()
