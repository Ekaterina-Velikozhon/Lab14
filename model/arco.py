from dataclasses import dataclass
from model.ordine import Ordine

@dataclass
class Arco:
    o1: Ordine
    o2: Ordine
    peso: int