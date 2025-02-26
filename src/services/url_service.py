def get_url(urls_db, id: str):
    for url in urls_db:
        if str(url["id"]) == id:
            return url
    return None
