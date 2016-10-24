from app import app
if __name__ == "__main__":
	app.run(debug=True,
			host=app.config.get("HOST", "localhost"),
			port=app.config.get("PORT", 556)
		)
