from app import app
app.run(host=app.config.get("HOST", "localhost"))
