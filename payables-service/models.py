from sqlalchemy import Column, String, Float, Date
from database import Base

class Invoice(Base):
    __tablename__ = "invoices"

    invoice_id = Column(String, primary_key=True, index=True)
    vendor_name = Column(String, nullable=False)
    vendor_email = Column(String, nullable=False)
    vendor_number = Column(String, nullable=False)
    invoice_date = Column(Date, nullable=False)
    due_date = Column(Date, nullable=False)
    amount = Column(Float, nullable=False)
    payment_method = Column(String, nullable=False)
    payment_status = Column(String, nullable=False)
    created_by = Column(String, nullable=False)

    def __repr__(self):
        return f"<Invoice(id={self.invoice_id}, vendor={self.vendor_name}, amount={self.amount})>"
