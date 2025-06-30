from flask import Flask, render_template
from config import Config
app = Flask(__name__)
app.config.from_object(Config)

@app.context_processor
def inject_settings():
    return {
        "settings": {
            "shop_name": app.config["SHOP_NAME"],
            "logo": app.config["LOGO_PATH"],
            "email": app.config["CONTACT_EMAIL"],
            "address": app.config["ADDRESS"]
        }
    }

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)
