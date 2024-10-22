from tabulate import tabulate
from dataclasses import dataclass


@dataclass
class Field:
    name: str
    value: str
    size: int
    ph_address: int


def format_fields(fields):
    table = tabulate([(field.name, field.value) for field in fields],
                     headers=['Field', 'Value'], tablefmt='plain')
    return table
