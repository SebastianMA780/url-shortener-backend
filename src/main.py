from fastapi import FastAPI
from .models import UrlData

app = FastAPI()

@app.get("/")
def read_root():
		return {"Hello": "World"}

@app.post("/api/shorten-url")
def shorten_url(url_data: UrlData):
		url_info = url_data.model_dump()
		return url_info
