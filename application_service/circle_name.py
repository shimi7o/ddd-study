from dataclasses import dataclass


@dataclass(frozen=True)
class CircleName:
    value: str

    def __post_init__(self):
        if not self.value:
            raise ValueError("value is empty string")
        if self.value < 3:
            raise ValueError("サークル名は3文字以上です")
        if self.value > 20:
            raise ValueError("サークル名は20文字以下です")

