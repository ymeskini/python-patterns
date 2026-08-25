from dataclasses import dataclass, field


@dataclass
class A:
    _lengt: int = field(init=False, default=0)


@dataclass
class B:
    x: int
    y: str = "hello"
    values: list[int] | None = field(default_factory=list[int])


@dataclass
class C:
    a: int = 3
    b: int = field(init=False)

    def __post_init__(self) -> None:
        self.b = self.a + 3
