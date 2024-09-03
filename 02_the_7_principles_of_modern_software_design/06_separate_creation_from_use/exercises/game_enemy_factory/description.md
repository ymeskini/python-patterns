Suppose you're building a game that involves creating different types of enemies such as knights, wizards, and archers. Each enemy has different attributes such as health, attack power, and defense. Here's an example of an Enemy class:

```python
from dataclasses import dataclass

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
```

Your game also has "spawn points" that spawn new enemies. There are three types of spawn points:

- Easy spawn points spawn enemies with low health, low attack power, and low defense. Easy spawn points only spawn knights and archers.
- Medium spawn points spawn enemies with medium health, medium attack power, and medium defense. Medium spawn points spawn knights, wizards, and archers.
- Hard spawn points spawn enemies with high health, high attack power, and high defense. Hard spawn points only spawn wizards.

a) Create a Python application that uses the Abstract Factory pattern to create enemies based on the type of spawn point (easy, medium, or hard). The application should print the attributes of the enemies that are created.

b) What would be a more functional way to create enemies based on the type of spawn point? Update your application to use this approach.
