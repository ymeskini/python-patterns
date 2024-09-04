from dataclasses import dataclass
from enum import StrEnum, auto


class EnemyType(StrEnum):
    KNIGHT = auto()
    ARCHER = auto()
    WIZARD = auto()


@dataclass
class Enemy:
    enemy_type: EnemyType
    health: int
    attack_power: int
    defense: int


def main() -> None:
    enemy = Enemy(EnemyType.KNIGHT, health=100, attack_power=10, defense=5)
    print(enemy)


if __name__ == "__main__":
    main()
