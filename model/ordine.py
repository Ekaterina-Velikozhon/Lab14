from dataclasses import dataclass
from datetime import date
@dataclass
class Ordine:
    order_id: int
    customer_id: int
    order_status: int
    order_date: date
    required_date: date
    shipped_date: date
    store_id: int
    staff_id: int

    def __hash__(self):
        return hash(self.order_id)

    def __eq__(self, other):
        if isinstance(other, int):
            return self.order_id == other
        elif isinstance(other, Ordine):  # Sostituisci con il vero nome della tua classe
            return self.order_id == other.order_id
        return False

    def __str__(self):
        return str(self.order_id)
