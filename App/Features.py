# Features.py

from flask import abort, make_response

from config import db
from models import Feature, Trail, feature_schema
from flask import request

def read_all():
    features = Feature.query.all()
    return feature_schema.dump(features)

def read_one(feature_id):
    feature = Feature.query.get(feature_id)

    if feature is not None:
        return feature_schema.dump(feature)
    else:
        abort(
            404, f"Feature with ID {feature_id} not found"
        )

def update(feature_id, feature):
    existing_feature = Feature.query.get(feature_id)

    if existing_feature:
        update_feature = feature_schema.load(feature, session=db.session)
        existing_feature.Feature_Name = update_feature.Feature_Name
        db.session.merge(existing_feature)
        db.session.commit()
        return feature_schema.dump(existing_feature), 200
    else:
        abort(404, f"Feature with ID {feature_id} not found")

def delete(feature_id):
    existing_feature = Feature.query.get(feature_id)

    if existing_feature:
        db.session.delete(existing_feature)
        db.session.commit()
        return make_response(f"{feature_id} successfully deleted", 204)
    else:
        abort(404, f"Feature with ID {feature_id} not found")

def create():
    feature = request.get_json()
    trail_id = feature.get("Trail_ID")
    trail = Trail.query.get(trail_id)

    if trail:
        new_feature = feature_schema.load(feature, session=db.session)
        trail.Features.append(new_feature)
        db.session.commit()
        return feature_schema.dump(new_feature), 201
    else:
        abort(
            404,
            f"Trail not found for ID: {trail_id}"
        )
