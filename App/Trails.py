# Trails.py

from flask import abort, make_response

from config import db
from models import Trail, trails_schema, trail_schema
from flask import request


def read_all():
    trails = Trail.query.all()
    return trails_schema.dump(trails)


def create():
    trail = request.get_json()
    trail_name = trail.get("Trail_Name")
    existing_trail = Trail.query.filter(Trail.Trail_Name == trail_name).one_or_none()

    if existing_trail is None:
        new_trail = trail_schema.load(trail, session=db.session)
        db.session.add(new_trail)
        db.session.commit()
        return trail_schema.dump(new_trail), 201
    else:
        abort(406, f"Trail with name {trail_name} already exists")


def read_one(trail_id):
    trail = Trail.query.filter(Trail.Trail_ID == trail_id).one_or_none()

    if trail is not None:
        return trail_schema.dump(trail)
    else:
        abort(404, f"Trail with ID {trail_id} not found")


def update(trail_id):
    trail = request.get_json() 
    existing_trail = Trail.query.filter_by(Trail_ID=trail_id).one_or_none()

    if existing_trail:
        for field, value in trail.items():
            setattr(existing_trail, field, value)
        db.session.commit()
        return trail_schema.dump(existing_trail), 200
    else:
        abort(404, f"Trail with ID {trail_id} not found")

def delete(trail_id):
    existing_trail = Trail.query.filter(Trail.Trail_ID == trail_id).one_or_none()

    if existing_trail:
        db.session.delete(existing_trail)
        db.session.commit()
        return make_response(f"{trail_id} successfully deleted", 200)
    else:
        abort(404, f"Trail with ID {trail_id} not found")
