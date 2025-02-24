def get_url(urls_db, id: str):
		print(urls_db)
		for url in urls_db:
				if str(url["id"]) == id:
						return url
		return None

	