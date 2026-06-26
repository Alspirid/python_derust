from dataclasses import dataclass


@dataclass
class Player:
    name: str
    score: int


def leaderboard(raw_data: list[tuple[str, int]], n: int) -> list[Player]:
    players = [Player(name, score) for name, score in raw_data]
    return sorted(players, key=lambda x: x.score, reverse=True)[:n]


raw = [("alice", 50), ("bob", 90), ("carol", 70), ("dave", 60)]
print(leaderboard(raw, 2))
# → [Player(name='bob', score=90), Player(name='carol', score=70)]
