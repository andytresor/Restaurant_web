from flask import render_template, request, redirect# type:ignore
from config import db
from Models.orders import Order

def index():
    orders = Order.query.all()
    return render_template('/displays/orders.html', title="Home Page", orders=orders)

def add_order():
    return render_template('/displays/add_orders.html', title="Add Order")

def view_order(id):
    orders = Order.query.get(id)
    return render_template('/displays/orders.html', title="User Detail Page", orders=orders)

def newOrder():
    form = request.form
    order_name = form['order_name']
    price = form['price']
    description = form['description']

    order = Order(order_name=order_name, price=price, description=description)
    db.session.add(order)
    db.session.commit()

    return redirect('/order')

def delete_order(id):
    if request.method == 'POST':
        if request.form['_method'] == 'DELETE':
            orders = Order.query.get(id)
            db.session.delete(orders)
            db.session.commit()
            return redirect('/order')
    

def update_Order(id):
    orders = Order.query.filter_by(id = id).first()
    if orders is None:
        return redirect('/order')
    if request.method == "GET":
        return  render_template('modify_orders.html', title="Update Order Page", orders=orders)
    elif request.method == "POST":
        form = request.form
        order_name = form['order_name']
        price = form['price']
        description = form['description']
        orders.name = order_name
        orders.email = price
        orders.phone = description
        db.session.commit()
        return redirect('/order')
    return render_template('modify.html', title="Update Order Page", orders=orders)
