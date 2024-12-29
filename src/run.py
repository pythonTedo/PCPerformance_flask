from flask import Flask
import os
from app.apis import api_blueprint
from app.views import views_blueprint

#app = create_app()
app = Flask(__name__, static_folder="app/static", template_folder="app/templates")
app.register_blueprint(api_blueprint)
app.register_blueprint(views_blueprint)

if __name__ == "__main__":
    
    print("Static Folder:", app.static_folder)
    port = int(os.environ.get("PORT", 5000))
    app.jinja_env.auto_reload = True
    app.config["TEMPLATES_AUTO_RELOAD"] = True
    app.run(debug=True, host = "0.0.0.0", port=port)