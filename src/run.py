from flask import Flask
import os
from app import create_app

app = create_app()


if __name__ == "__main__":
    print("Registered Routes:", app.url_map)
    port = int(os.environ.get("PORT", 5000))
    app.jinja_env.auto_reload = True
    app.config["TEMPLATES_AUTO_RELOAD"] = True
    app.run(debug=True, host = "0.0.0.0", port=port)