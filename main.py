from fastapi import FastAPI

# для html
from starlette.templating import Jinja2Templates


from user.user_api import user_router
from card.card_api import card_router
from transfers.transfers_api import transaction_router

# Создать базу данных
from database import Base, engine
Base.metadata.create_all(bind=engine)
#######

app = FastAPI(docs_url='/')

## Если хотим выводить html страницы
template = Jinja2Templates(directory='templates')

from html_example.html_show import html_router
app.include_router(html_router)
####

# Регистрация компонентов
app.include_router(user_router)
app.include_router(card_router)
app.include_router(transaction_router)

