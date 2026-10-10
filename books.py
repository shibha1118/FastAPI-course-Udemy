from fastapi import FastAPI
from fastapi import Body

app = FastAPI()

BOOKS = [
    {'title': 'Title one', 'author': 'Author one', 'category': 'Science'},
    {'title': 'Title two', 'author': 'Author one', 'category': 'Science'},
    {'title': 'Title three', 'author': 'Author three', 'category': 'History'},
    {'title': 'Title four', 'author': 'Author four', 'category': 'math'},
    {'title': 'Title five', 'author': 'Author five', 'category': 'math'},
    {'title': 'Title six', 'author': 'Author two', 'category': 'math'}
]

@app.get("/books")
async def read_all_books():
    return BOOKS

@app.get("/books/{dynamic_param}")
async def read_all_books(dynamic_param: str):
    return {"dynamic_param": dynamic_param}

@app.post("/books/new_book")
async def create_new_book(new_book = Body()):
    BOOKS.append(new_book)

@app.put("/books/update_book")
async def update_that_book(update_book = Body()):
    for i in range(len(BOOKS)):
        if BOOKS[i].get('title').casefold() == update_book.get('title').casefold():
            BOOKS[i] = update_book

@app.delete("/books/delete_book/{fry}")
async def fry_that_book(fry:str):
    for i in range(len(BOOKS)):
        if BOOKS[i].get('title').casefold() == fry.casefold():
            BOOKS.pop(i)
            break