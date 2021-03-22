from dataclasses import dataclass


@dataclass(frozen=True)
class CircleId:
    value: str

    def __post_init__(self):
        if not self.value:
            raise ValueError("value is empty string")
