from pydantic import BaseModel, EmailStr
from datetime import date

class InvoiceCreate(BaseModel):
    invoice_id: str
    vendor_name: str
    vendor_email: EmailStr
    vendor_number: str
    invoice_date: date
    due_date: date
    amount: float
    payment_method: str
    payment_status: str
    created_by: str

class InvoiceResponse(InvoiceCreate):
    class Config:
        orm_mode = True
