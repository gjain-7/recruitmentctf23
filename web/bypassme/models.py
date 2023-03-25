import random
from dataclasses import dataclass, field
from typing import Optional


@dataclass
class User:
    id: int
    username: str
    password: str
