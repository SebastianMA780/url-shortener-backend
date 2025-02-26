from fastapi import APIRouter
from fastapi.responses import RedirectResponse
from ..models.url_data import UrlData
from ..services.url_service import get_url

router = APIRouter()
urls_db = []
APP_SHORT_DOMAIN = "http://localhost:8000"

@router.get("/")
def read_root():
    return {"Hello": "World"}

@router.post("/api/shorten-url")
def shorten_url(url_data: UrlData):
    url_info = url_data.model_dump()
    url_id = len(urls_db) + 1
    urls_db.append({
        "id": url_id,
        "url": url_info["url"]
    })
    return {"short_url": f"{APP_SHORT_DOMAIN}/{url_id}"}

@router.get("/{url_id}")
def url_redirect(url_id: str):
    url = get_url(urls_db, url_id)
    if url is None:
        return {"error": "URL not found"}
    return RedirectResponse(url["url"], status_code=302)