from paytrack.domain.models import Payment
from paytrack.domain.repository import PaymentRepository
from datetime import datetime

class PaymentService:

    def __init__(self, repo: PaymentRepository):
        print("🔌 Conexión al repositorio establecida.")
        self.repo = repo
        self.counter = 1

    def registrar_pago(self, nombre_cliente: str, monto: float) -> Payment:
        if monto <= 0:
            raise ValueError("El monto debe ser mayor que cero")
        pago = Payment(id=self.counter, nombre_cliente=nombre_cliente, monto=monto, fecha=datetime.now())
        self.counter += 1
        return self.repo.save(pago)

    def listar_pagos(self):
        return self.repo.get_all()

    def buscar_por_cliente(self, nombre_cliente: str):
        return self.repo.find_by_client(nombre_cliente)

    def eliminar_pago(self, payment_id: int):
        pago = self.repo.get_by_id(payment_id)
        if not pago:
            raise ValueError("Pago no encontrado")
        if pago.estado != "COMPLETADO":
            raise ValueError("No se puede eliminar un pago no completado")
        return self.repo.delete(payment_id)