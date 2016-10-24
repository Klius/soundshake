from app import app
app.run(debug=True,
			host=app.config.get("HOST", "localhost"))
