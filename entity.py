import dataclasses


@dataclasses.dataclass()
class FullName:
    id: str
    family_name: str
    first_name: str

full_name1 = FullName("matsuoka", "kota")

print(full_name1)