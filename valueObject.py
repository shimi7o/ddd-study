import dataclasses


@dataclasses.dataclass(frozen=True)
class FullName:
    family_name: str
    first_name: str

full_name1 = FullName("matsuoka", "kota")
