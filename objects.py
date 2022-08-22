from dataclasses import dataclass


@dataclass
class Dimensions:
    lines: int
    stripes: int


@dataclass
class Element:
    line: int
    stripe: int
