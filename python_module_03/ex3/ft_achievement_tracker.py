#!/usr/bin/env python3
def all_achievements(players: list) -> set:
    """Return a set of all the achievement of all the players"""
    achievements = set()
    for p in players:
        for a in p:
            achievements.add(a)
    return achievements


def common_achievement(players: list) -> set:
    """Search the common achievement on the list of players"""
    achievements = players[0]
    for p in players:
        achievements: set = achievements.intersection(p)
    return achievements


def rare_achievement(players: list) -> set:
    """Search wich achievements only has 1 player"""
    achievements = set()
    for current_ply in players:
        other_achievements = set()
        for other_ply in players:
            if other_ply is not current_ply:
                print(f"{other_ply} union {other_achievements}")
                other_achievements = other_achievements.union(other_ply)
                print(f"result: {other_achievements}")
        print(f"\n{current_ply} difference {other_achievements}")
        unique = current_ply.difference(other_achievements)
        print(f"{unique}\n")
        achievements = achievements.union(unique)
    return achievements


def uniques_achievements(players: list) -> set:
    """Return the uniques achievements of all the players"""
    return all_achievements(players)


def player_uniques_achievements(target: set, players: list) -> set:
    """Return the unique items of target player"""
    other_achievements = set()
    for p in players:
        if p is not target:
            other_achievements = other_achievements.union(p)
    return target.difference(other_achievements)


def ft_achievement_tracker():
    print("=== Achievement Tracker System ===\n")
    alice = set(["first_kill", "level_10", "treasure_hunter", "speed_demon"])
    bob = set(["first_kill", "level_10", "boss_slayer", "collector"])
    charlie = set(["level_10", "treasure_hunter", "boss_slayer",
                   "speed_demon", "perfectionist"])

    players = [alice, bob, charlie]

    print(f"Player alice achievements: {alice}")
    print(f"Player bob achievements: {bob}")
    print(f"Player charlie achievements: {charlie}")

    print("\n=== Achievement Analytics ===")
    achievements = uniques_achievements(players)
    print(f"All unique achievements: {achievements}")
    print(f"Total unique achievements {len(achievements)}")

    print(f"\nCommon to all players: {common_achievement(players)}")
    print(f"Rare achievements (1 player): {rare_achievement(players)}")

    vs = [alice, bob]
    print(f"\nAlice vs Bob common: {common_achievement(vs)}")
    print(f"Alice unique: {player_uniques_achievements(alice,vs)}")
    print(f"Bob unique: {player_uniques_achievements(bob,vs)}")


# if __name__ == "__main__":
#     ft_achievement_tracker()
