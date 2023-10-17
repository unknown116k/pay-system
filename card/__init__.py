from pydantic import BaseModel


# Класс для валидации добавления карты (user_id, card_number, balance, card_name, exp_date, cvv)
class CardAddModel(BaseModel):
    user_id: int
    card_number: int
    balance: float
    card_name: str
    exp_date: int
    cvv: int

# Класс для валидации изменения дизайна карты (card_from, card_to, amount)
class EditCardModel(BaseModel):
    card_id: int
    design_path: str


