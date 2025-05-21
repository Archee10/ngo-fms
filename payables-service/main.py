from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from database import engine, SessionLocal
import models, schemas
from sqlalchemy.exc import IntegrityError

# Create tables
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/invoices", response_model=schemas.InvoiceResponse, status_code=201)
def create_invoice(invoice: schemas.InvoiceCreate, db: Session = Depends(get_db)):
    if invoice.amount <= 0:
        raise HTTPException(status_code=400, detail="Amount must be greater than 0")

    db_invoice = models.Invoice(**invoice.dict())
    db.add(db_invoice)
    try:
        db.commit()
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=400, detail="Invoice ID already exists")
    db.refresh(db_invoice)
    return db_invoice
