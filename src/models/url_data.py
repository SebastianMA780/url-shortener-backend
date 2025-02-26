from pydantic import BaseModel, HttpUrl

class UrlData(BaseModel):
    url: HttpUrl
