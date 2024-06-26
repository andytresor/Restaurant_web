from flask import render_template, request, redirect# type:ignore
from config import db
from Models.orders import Order
# from Models.users import User

# def user_id():
#     users = User.query.get(id)
#     return render_template('/menu/add_menu.html', user=users)

def index():
    orders = Order.query.all()
    return render_template('/displays/orders.html', title="Home Page", orders=orders)

def add_order():
    return render_template('/orders/add_orders.html', title="Add Order")

def view_order(id):
    orders = Order.query.get(id)
    return render_template('/displays/orders.html', title="User Detail Page", orders=orders)

def newOrder():
    form = request.form
    menu_name = form['menu_name']
    price = form['price']
    description = form['description']

    orders = Order(menu_name=menu_name, price=price, description=description)
    db.session.add(orders)
    db.session.commit()

    return redirect('/menu/menu')

def delete_order(order_id):
    if request.method == 'POST':
        if request.form['_method'] == 'DELETE':
            orders = Order.query.get(order_id)
            db.session.delete(orders)
            db.session.commit()
            return redirect('/order/order')
    

def update_Order(order_id):
    orders = Order.query.filter_by(order_id = order_id).first()
    if orders is None:
        return redirect('/order/order')
    if request.method == "GET":
        return  render_template('modify_orders.html', title="Update Order Page", orders=orders)
    elif request.method == "POST":
        form = request.form
        menu_name = form['menu_name']
        price = form['price']
        description = form['description']
        orders.menu_name = menu_name
        orders.email = price
        orders.phone = description
        db.session.commit()
        return redirect('/order/order')
    return render_template('modify.html', title="Update Order Page", orders=orders)
