from flask import render_template, request, redirect# type:ignore
from config import db
from Models.staff import Staff

def index():
    users = Staff.query.all()
    return render_template('index.html', title="Home Page", users=users)

def add_staff():
    return render_template('staff/add_staff.html', title="Add Staff")

def view_staff(id):
    users = Staff.query.get(id)
    return render_template('display/staff.html', title="User Detail Page", users=users)

def newStaff():
    form = request.form
    name = form['name']
    email = form['email']
    salary = form['salary']
    role = form['role']

    user = Staff(name=name, email=email, salary=salary, role=role)
    db.session.add(user)
    db.session.commit()

    return redirect('/staff')

def delete_staff(id):
    if request.method == 'POST':
        if request.form['_method'] == 'DELETE':
            users = Staff.query.get(id)
            db.session.delete(users)
            db.session.commit()
            return redirect('/staff')
    

def update_staff(id):
    users = Staff.query.filter_by(id = id).first()
    if users is None:
        return redirect('/staff')
    if request.method == "GET":
        return  render_template('modify_staff.html', title="Update Page", users=users)
    elif request.method == "POST":
        form = request.form
        name = form['name']
        email = form['email']
        salary = form['salary']
        role = form['role']
        users.name = name
        users.email = email
        users.salary = salary
        users.role = role
        db.session.commit()
        return redirect('/staff')
    return render_template('modify_staff.html', title="Update Page", users=users)
