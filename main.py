from typing import Union
import json
from fastapi import FastAPI, Response, HTTPException
from pathlib import Path

app = FastAPI()

data = []
with open("data/log.json", "r", encoding="utf-8") as file:
    data = json.loads(file.read())

types = {}

with open("data/shinigami.json", "r", encoding="utf-8") as file:
    types["shinigami"] = json.loads(file.read())

with open("data/arrancar.json", "r", encoding="utf-8") as file:
    types["arrancar"] = json.loads(file.read())

with open("data/humans.json", "r", encoding="utf-8") as file:
    types["humans"] = json.loads(file.read())

with open("data/quincy.json", "r", encoding="utf-8") as file:
    types["quincy"] = json.loads(file.read())


@app.get("/")
def read_root():
    return {
        "name": "Bleach API",
        "description": "This is the API for Bleach Anime.",
        "supports": ["shinigami", "humans", "quincy", "arrancar"],
        "author": "AshishK1331",
        "contact": "http://github.com/ashishk1331",
    }


@app.get("/characters")
def read_characters():
    return {"types": list(data.keys())}


@app.get("/characters/{type_id}")
def read_character_type(type_id: str):
    return {type_id: list(set(data[type_id]))}


@app.get("/characters/{type_id}/{name}")
def read_character_type(type_id: str, name: str):
    results = []
    for i in types[type_id]:
        if i["id"].find(name) > -1:
            results.append(i)
    return {"results": results}


@app.get("/avatar/{race}/{slug}")
def display_avatar(race: str, slug: str):
    image_path = Path(f"images/{race}/{slug}.png")

    if not image_path.is_file():
        raise HTTPException(status_code=404, detail="Image not found")

    try:
        with open(f"images/{race}/{slug}.png", "rb") as f:
            image_data = f.read()
        return Response(content=image_data, media_type="image/png")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error reading image: {e}")
