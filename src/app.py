from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates


app = FastAPI()

app.mount("/static", StaticFiles(directory="src/static"), name="static")
templates = Jinja2Templates(directory="src/views")
index = Jinja2Templates(directory="src/")

@app.get("/")
async def page_slash_home():
    return RedirectResponse("/home")

@app.get("/home", response_class=HTMLResponse)
async def page_home(request: Request):
    return index.TemplateResponse(request=request, name="index.html")

@app.get("/contacto", response_class=HTMLResponse)
async def page_contacto(request: Request):
    return templates.TemplateResponse(request=request, name="contacto.html")

@app.get("/presupuesto", response_class=HTMLResponse)
async def page_presupuesto(request: Request):
    return templates.TemplateResponse(request=request, name="presupuesto.html")

@app.get("/products", response_class=HTMLResponse)
async def page_products(request: Request):
    return templates.TemplateResponse(request=request, name="products.html")