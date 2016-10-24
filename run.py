#!flask/bin/python
from app import app
app.run(debug=True,
			host=app.config.get("HOST", "localhost"),
			port=app.config.get("PORT", 556)
		)
