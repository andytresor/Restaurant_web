from flask import render_template, request, redirect# type:ignore
from config import db
from Models.owner import Owner

def index():
    owners = Owner.query.all()
    return render_template('index.html', title="Display Page", owners=owners)

# def add_owner():
#     return render_template('add_owner.html', title="Add Owner")


# def newUser():
#     form = request.form
#     name = form['name']
#     email = form['email']
#     phone = form['phone']

#     user = Owner(name=name, email=email, phone=phone)
#     db.session.add(user)
#     db.session.commit()

#     return redirect('/display')

# def delete_user(id):
#     if request.method == 'POST':
#         if request.form['_method'] == 'DELETE':
#             users = Utilisateur.query.get(id)
#             db.session.delete(users)
#             db.session.commit()
#             return redirect('/display')
    
#     users = Utilisateur.query.filter_by(id = id).first()
#     if users is None:
#         return redirect('/display')
#     if request.method == "GET":
#         return  render_template('user_update.html', title="Update Page", users=users)
#     elif request.method == "POST":
#         form = request.form
#         name = form['name']
#         email = form['email']
#         phone = form['phone']
#         users.name = name
#         users.email = email
#         users.phone = phone
#         db.session.commit()
#         return redirect('/display')
#     return render_template('user_update.html', title="Update Page", users=users)
