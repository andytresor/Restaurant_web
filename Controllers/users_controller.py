from flask import render_template, redirect, request, session # type: ignore
from Models.users import User
from werkzeug.security import generate_password_hash, check_password_hash
from config import db

def login():
    return render_template('/auth/login.html')

def login_user():
     form = request.form
     email = form['email']
     password = form['password']
     user_type = form['User_type']
     
     user = User.query.filter_by(email=email).first()
     if not user or not check_password_hash(user.password, password):
         return redirect('auth/login', message="invalid Credential!!")
     if user.User_type != user_type:
         return redirect('auth/login', message="invalid Credential!!")
     if user_type == "Admin":
         return redirect('/reservation/reservation')
     session['auth'] = {
        "id": user.user_id,
        "username": user.user_name
    }
     return redirect('/menu/menu')
          
     

#Register

def register():
    return render_template('/auth/register.html')

def register_user():
     form = request.form
     user_name = form['user_name']
     email = form['email']
     User_type = form['User_type']
     password = form['password']
     cpassword = form['cpassword']

     if password != cpassword:
         return redirect('/auth/register', message="Invalid Password")
     
     user = User.query.filter_by(email=email).first()
     if user:
         return redirect('/auth/register', message="User with this email aready exists!!")
     
     user = User(email=email, user_name=user_name, User_type=User_type, password=generate_password_hash(password))
     db.session.add(user)
     db.session.commit()
     return redirect('/auth/login')
     
     

#logout

def logout():
    if 'auth' in  session:
        session.pop('auth', None)
    return redirect('/auth/login')


