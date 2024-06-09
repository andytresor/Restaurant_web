from flask import render_template, request, redirect# type:ignore
from config import db
from Models.menu import Menu

# def style():
#     return render_template('/Styles/display.css')
def index():
    menus = Menu.query.all()
    return render_template('/displays/menu.html', title="Menu Page", menus=menus)

def add_menu():
    return render_template('/menu/add_menu.html', title="Add Menu")

def view_menu(id):
    menus = Menu.query.get(id)
    return render_template('/display/menu.html', title="User Detail Page", menus=menus)

def newMenu():
    form = request.form
    menu_name = form['menu_name']
    price = form['price']
    description = form['description']

    menu = Menu(menu_name=menu_name, price=price, description=description)
    db.session.add(menu)
    db.session.commit()

    return redirect('/menu/menu')

def delete_menu(id):
    if request.method == 'POST':
        if request.form['_method'] == 'DELETE':
            menus = Menu.query.get(id)
            db.session.delete(menus)
            db.session.commit()
            return redirect('/menu')
    

def update_menu(id):
    menus = Menu.query.filter_by(id = id).first()
    if menus is None:
        return redirect('/menu')
    if request.method == "GET":
        return  render_template('user_update.html', title="Update Page", menus=menus)
    elif request.method == "POST":
        form = request.form
        menu_name = form['menu_name']
        price = form['price']
        description = form['description']
        menus.name = menu_name
        menus.email = price
        menus.phone = description
        db.session.commit()
        return redirect('/menu')
    return render_template('modify.html', title="Update Menu Page", menus=menus)
