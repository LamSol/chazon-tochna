from flask import Flask, render_template,request, redirect, url_for,flash
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

@app.route('/feedback',methods=['GET','POST'])
def feedback():
    if request.method == 'POST':
        name = request.form['name']
        message = request.form['message']
        print(f"feedback from {name}: {message}")
        flash('Thank you for your feedback!')
        return redirect(url_for('feedback'))
    return render_template('feedback.html')

app.secret_key = 'supersecretkey' # to be changed later for production

@app.route('/customer/<int:id>')
def view_customer(id):
    return f"Customer ID: {id}"

@app.route('/invoice/<int:id>')
def view_invoice(id):
    return f"Invoice ID: {id}"

@app.route('/product/<int:id>')
def view_product(id):
    return f"Product ID:{id}"

@app.route('/search/<string:query>')
def search(query):
    return f"Search results for: {query}"

@app.route('/category/<path:category_name>')
def category(category_name):
    return f"Category path: {category_name}"

if __name__ == '__main__':
    app.run(debug=True)
