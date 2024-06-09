from flask import render_template, request, redirect# type:ignore
from config import db
from Models.client import Client

def index():
    users = Client.query.all()
    return render_template('index.html', title="Home Page", users=users)

def add_user():
    return render_template('/displays/add_client.html', title="client")

# def view(id):
#     users = Client.query.get(id)
#     return render_template('user_detail.html', title="User Detail Page", users=users)

def newUser():
    form = request.form
    name = form['name']
    email = form['email']

    user = Client(name=name, email=email)
    db.session.add(user)
    db.session.commit()

    return redirect('/add_menu')

# def delete_user(id):
#     if request.method == 'POST':
#         if request.form['_method'] == 'DELETE':
#             users = Client.query.get(id)
#             db.session.delete(users)
#             db.session.commit()
#             return redirect('/display')
    

# def update_user(id):
#     users = Client.query.filter_by(id = id).first()
#     if users is None:
#         return redirect('/display')
#     if request.method == "GET":
#         return  render_template('user_update.html', title="Update Page", users=users)
#     elif request.method == "POST":
#         form = request.form
#         name = form['name']
#         email = form['email']
#         users.name = name
#         users.email = email
#         db.session.commit()
#         return redirect('/display')
#     return render_template('user_update.html', title="Update Page", users=users)
