from app import app
app.run(host=app.config.get("HOST", "localhost"),
		port=app.config.get("PORT","80")
		)
