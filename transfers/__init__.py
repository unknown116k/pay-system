from pydantic import BaseModel



# Класс для валидации создания перевода
class CreateTransactionModel(BaseModel):
    card_from: int
    card_to: int
    amount: float

# Класс для валидации отмена перевода
class CancelTransactionModel(BaseModel):
    card_from: str
    card_to: str
    amount: float
    transfer_id: int