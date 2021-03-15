from dataclasses import dataclass

@dataclass(frozen=True)
class FullName:
    family_name: str
    first_name: str

    def __post_init__(self):
        if not self.family_name:
            raise ValueError('family name is empty string')
        if not self.first_name:
            raise ValueError('first name is empty string')

full_name = FullName("a", "a")

print(full_name.family_name)