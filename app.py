import os
import secrets
import sqlalchemy.dialects.postgresql
from flask import Flask, flash
from flask import render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, DecimalField
from wtforms.validators import DataRequired

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('POSTGRES_URL')
db = SQLAlchemy(app)
app.config['SECRET_KEY'] = secrets.token_hex(16)


# Define the database models
class Cart(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    cart_items = db.relationship('CartItem', backref='cart', lazy=True)


class CartItem(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    item = db.Column(db.String(255))
    price = db.Column(db.Float)
    cart_id = db.Column(db.Integer, db.ForeignKey('cart.id'))


class CartItemForm(FlaskForm):
    item = StringField('Item', validators=[DataRequired()])
    price = DecimalField('Price', validators=[DataRequired()])


with app.app_context():
    db.create_all()


@app.route('/', methods=['GET', 'POST'])
def cart():
    form = CartItemForm(request.form)

    if request.method == 'POST' and form.validate():
        items = request.form.getlist('item')
        prices = request.form.getlist('price')

        # Create a cart
        cart = Cart()
        db.session.add(cart)
        db.session.commit()

        # Create and add cart items
        for item, price in zip(items, prices):
            cart_item = CartItem(item=item, price=price, cart=cart)
            db.session.add(cart_item)

        db.session.commit()

        return redirect(url_for('summary', cart_id=cart.id))

    return render_template('cart.html', form=form)


@app.route('/summary/<int:cart_id>')
def summary(cart_id):
    cart = Cart.query.filter_by(id=cart_id).first()
    if not cart:
        return render_template('404.html'), 404
    cart_items = CartItem.query.filter_by(cart_id=cart_id)
    total_price = sum(item.price for item in cart_items)
    return render_template('summary.html', total_price=total_price, cart_id=cart_id)


@app.route('/edit/<int:cart_id>', methods=['GET', 'POST'])
def edit_cart(cart_id):
    cart = Cart.query.filter_by(id=cart_id).first()
    if not cart:
        return render_template('404.html'), 404
    cart_items = CartItem.query.filter_by(cart_id=cart_id).all()

    if request.method == 'POST':
        try:
            # Delete existing cart items for the given cart_id
            CartItem.query.filter_by(cart_id=cart_id).delete()

            # Process and save the edited cart items
            for i, cart_item in enumerate(cart_items):
                item = request.form.get(f'item_{i}')
                price = request.form.get(f'price_{i}')
                if item and price:
                    edited_item = CartItem(item=item, price=price, cart_id=cart_id)
                    db.session.add(edited_item)

            # Process and save the new items
            num_new_items = len(request.form.getlist('item_new[]'))
            for i in range(num_new_items):
                item = request.form.getlist('item_new[]')[i]
                price = request.form.getlist('price_new[]')[i]
                if item and price:
                    new_item = CartItem(item=item, price=price, cart_id=cart_id)
                    db.session.add(new_item)

            db.session.commit()

            flash('Cart updated successfully!', 'success')
            return redirect(url_for('summary', cart_id=cart_id))
        except Exception as e:
            flash(f'An error occurred: {str(e)}', 'error')

    form = CartItemForm(request.form)

    return render_template('edit_cart.html', cart_items=cart_items, form=form, cart_id=cart_id)


if __name__ == '__main__':
    app.run(debug=True)