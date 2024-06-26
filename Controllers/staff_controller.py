from flask import render_template, request, redirect# type:ignore
from config import db
from Models.staff import Staff

# def user_id():
#     users = User.query.get(id)
#     return render_template('/menu/add_menu.html', user=users)

def index():
    users = Staff.query.all()
    return render_template('/displays/staff.html', title="Home Page", users=users)

def add_staff():
    return render_template('/staff/add_staff.html', title="Add Staff")

def view_staff(id):
    users = Staff.query.get(id)
    return render_template('/displays/staff.html', title="User Detail Page", users=users)

def newStaff():
    form = request.form
    name = form['name']
    email = form['email']
    salary = form['salary']
    role = form['role']

    user = Staff(name=name, email=email, salary=salary, role=role)
    db.session.add(user)
    db.session.commit()

    return redirect('/reservation/reservation')

def delete_staff(staff_id):
    if request.method == 'POST':
        if request.form['_method'] == 'DELETE':
            users = Staff.query.get(staff_id)
            db.session.delete(users)
            db.session.commit()
            return redirect('/staff/staff')
    

def update_staff(staff_id):
    users = Staff.query.filter_by(staff_id = staff_id).first()
    if users is None:
        return redirect('/staff/staff')
    if request.method == "GET":
        return  render_template('/staff/modify_staff.html', title="Update Page", users=users)
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
        return redirect('/staff/staff')
    return render_template('/staff/modify_staff.html', title="Update Page", users=users)
