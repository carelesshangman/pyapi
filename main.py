from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
import json

app = FastAPI()

class Person(BaseModel):
    id: Optional[int] = None
    name: str
    age: int
    education: str

with open('people.json', 'r') as f:
    people = json.load(f)['people']

@app.get('/person/{p_id}')
def getPerson(p_id: int):
    person = [p for p in people if p['id'] == p_id]
    return person[0] if len(person) > 0 else {}

@app.post('/add/{p_name}{p_age}{p_education}')
def addPerson(p_name: str, p_age: int, p_education):