from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
from paytrack.use_cases.payment_service import PaymentService
from paytrack.adapters.output.in_memory_repository import InMemoryPaymentRepository
from datetime import datetime

app = FastAPI()

# Modelos de entrada/salida para la API
class PaymentIn(BaseModel):
    nombre_cliente: str
    monto: float

class PaymentOut(BaseModel):
    id: int
    nombre_cliente: str
    monto: float
    fecha: datetime
    estado: str

# Inicializar servicios
repo = InMemoryPaymentRepository()
service = PaymentService(repo)

@app.post("/pagos", response_model=PaymentOut, status_code=201)
def registrar_pago(pago: PaymentIn):
    try:
        nuevo_pago = service.registrar_pago(pago.nombre_cliente, pago.monto)
        return nuevo_pago
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/pagos", response_model=List[PaymentOut])
def listar_pagos():
    return service.listar_pagos()

@app.get("/pagos/cliente/{nombre_cliente}", response_model=List[PaymentOut])
def pagos_por_cliente(nombre_cliente: str):
    return service.buscar_por_cliente(nombre_cliente)

@app.delete("/pagos/{pago_id}", status_code=204)
def eliminar_pago(pago_id: int):
    try:
        service.eliminar_pago(pago_id)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))