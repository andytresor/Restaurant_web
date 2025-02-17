from flask import render_template, request, redirect# type:ignore
from config import db
from Models.reservation import Reservation

def index():
    reservations = Reservation.query.all()
    return render_template('/displays/reservation.html', title="Reservation Page", reservations=reservations)

def add_reservation():
    return render_template('/reservation/add_reservation.html', title="Add Reservation")

def view_reservation(id):
    reservations = Reservation.query.get(id)
    return render_template('/reservation/modify_reservation.html', title="Reservation Detail Page", reservations=reservations)

def newReservation():
    form = request.form
    table_name = form['name']
    price = form['price']
    description = form['description']
    print(reservation)

    reservation = Reservation(table_name=table_name, price=price, description=description)
    db.session.add(reservation)
    db.session.commit()

    return redirect('/reservation/reservation')

def delete_reservation(id):
    if request.method == 'POST':
        if request.form['_method'] == 'DELETE':
            reservations = Reservation.query.get(id)
            db.session.delete(reservations)
            db.session.commit()
            return redirect('/reservation/reservation')
    

def update_reservation(id):
    reservations = Reservation.query.filter_by(id = id).first()
    if reservations is None:
        return redirect('/reservation/reservation')
    if request.method == "GET":
        return  render_template('/reservation/modify_reservation.html', title="Update Page", reservations=reservations)
    elif request.method == "POST":
        form = request.form
        table_name = form['table_name']
        price = form['price']
        description = form['description']
        reservations.name = table_name
        reservations.email = price
        reservations.phone = description
        db.session.commit()
        return redirect('/reservation/reservation')
    return render_template('user_update.html', title="Update Page", reservations=reservations)
