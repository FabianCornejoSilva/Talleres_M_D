from paytrack.domain.repository import PaymentRepository
from paytrack.domain.models import Payment

class InMemoryPaymentRepository(PaymentRepository):
    def __init__(self):
        print("🗃️ Repositorio en memoria inicializado.")
        self.pagos = {}

    def save(self, payment: Payment) -> Payment:
        self.pagos[payment.id] = payment
        return payment

    def get_all(self):
        return list(self.pagos.values())

    def find_by_client(self, nombre_cliente: str):
        return [p for p in self.pagos.values() if p.nombre_cliente.lower() == nombre_cliente.lower()]

    def get_by_id(self, payment_id: int):
        return self.pagos.get(payment_id)

    def delete(self, payment_id: int):
        if payment_id in self.pagos:
            del self.pagos[payment_id]
            return True
        return False