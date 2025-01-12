# Trails.py

from flask import abort, make_response

from config import db
from models import Trail, trails_schema, trail_schema


def read_all():
    trails = Trail.query.all()
    return trails_schema.dump(trails)


def create(trail):
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


def update(trail_id, trail):
    existing_trail = Trail.query.filter(Trail.Trail_ID == trail_id).one_or_none()

    if existing_trail:
        update_trail = trail_schema.load(trail, session=db.session)
        existing_trail.Trail_Name = update_trail.Trail_Name
        existing_trail.Trail_Location = update_trail.Trail_Location
        existing_trail.Trail_Rating = update_trail.Trail_Rating
        existing_trail.Trail_Difficulty = update_trail.Trail_Difficulty
        existing_trail.Trail_Length_KM = update_trail.Trail_Length_KM
        existing_trail.Trail_Elevation_Gain_M = update_trail.Trail_Elevation_Gain_M
        existing_trail.Trail_Route_Type = update_trail.Trail_Route_Type
        existing_trail.Trail_Estimated_Finish_Time_Min = update_trail.Trail_Estimated_Finish_Time_Min
        existing_trail.Trail_Summary = update_trail.Trail_Summary
        existing_trail.Trail_Description = update_trail.Trail_Description
        existing_trail.Email_address = update_trail.Email_address
        existing_trail.Point1_lat = update_trail.Point1_lat
        existing_trail.Point1_long = update_trail.Point1_long
        existing_trail.Point1_Desc = update_trail.Point1_Desc
        existing_trail.Point2_lat = update_trail.Point2_lat
        existing_trail.Point2_long = update_trail.Point2_long
        existing_trail.Point2_Desc = update_trail.Point2_Desc
        existing_trail.Point3_lat = update_trail.Point3_lat
        existing_trail.Point3_long = update_trail.Point3_long
        existing_trail.Point3_Desc = update_trail.Point3_Desc
        existing_trail.Point4_lat = update_trail.Point4_lat
        existing_trail.Point4_long = update_trail.Point4_long
        existing_trail.Point4_Desc = update_trail.Point4_Desc
        existing_trail.Point5_lat = update_trail.Point5_lat
        existing_trail.Point5_long = update_trail.Point5_long
        existing_trail.Point5_Desc = update_trail.Point5_Desc
        db.session.merge(existing_trail)
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
