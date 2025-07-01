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

@app.route('/product/create', methods = ['GET','POST'])
def create_product():
    if request.method == 'POST':
        name=request.form['name']
        category = request.form['category']
        price = request.form['price']
        stock = request.form['stock']

        # The codes below would later be changed after building the database.
        print(f"[PRODUCT] {name} | {category} | ₹{price} | Stock: {stock}")
        flash('New Product created successfully!')
        return redirect(url_for('create_product'))
    return render_template('product_create.html')

@app.route('/customer/register', methods=['GET', 'POST'])
def register_customer():
    if request.method == 'POST':
        name = request.form['name']
        phone = request.form['phone']
        email = request.form['email']
        
        print(f"[CUSTOMER] {name} | {phone} | {email}")
        flash('Customer registered successfully!')
        return redirect(url_for('register_customer'))

    return render_template('customer_register.html')


if __name__ == '__main__':
    app.run(debug=True)
