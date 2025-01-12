# TrailUsers.py

from flask import abort, make_response

from config import db
from models import TrailUser, trail_user_schema


def read_one(email_address):
    trailuser = TrailUser.query.filter_by(email_address)

    if trailuser is not None:
        return trail_user_schema.dump(trailuser)
    else:
        abort(
            404, f"User with the address {email_address} not found"
        )

def update(email_address, trailuser):
    existing_trailuser  = TrailUser.query.filter_by(email_address=email_address).one_or_none()

    if existing_trailuser:
        update_trailuser = trail_user_schema.load(trailuser, session=db.session)
        existing_trailuser.UserName = update_trailuser.UserName
        existing_trailuser.Email_address = update_trailuser.Email_address
        existing_trailuser.UserRole = update_trailuser.UserRole
        db.session.merge(existing_trailuser)
        db.session.commit()
        return trail_user_schema.dump(existing_trailuser), 200
    else:
        abort(404, f"Trail user with address {email_address} not found")

def delete(email_address):
    existing_trailuser = TrailUser.query.filter_by(email_address)

    if existing_trailuser:
        db.session.delete(existing_trailuser)
        db.session.commit()
        return make_response(f"{email_address} successfully deleted", 204)
    else:
        abort(404, f"Trail user with address {email_address} not found")

def create(trailuser):
    email_address = trailuser.get("email_address")
    existing_trailuser = TrailUser.query.filter(TrailUser.Email_address == email_address).one_or_none()
    user_name = trailuser.get("username")
    existing_trailuser = TrailUser.query.filter(TrailUser.UserName == user_name).one_or_none()

    if existing_trailuser is None:
        new_trailuser = trail_user_schema.load(trailuser, session=db.session)
        db.session.add(new_trailuser)
        db.session.commit()
        return trail_user_schema.dump(new_trailuser), 201
    else:
        abort(406, f"User with name {username} or address {email_address} already exists")
