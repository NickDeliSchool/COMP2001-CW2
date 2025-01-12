#models.py

import pytz
from datetime import datetime
from marshmallow_sqlalchemy import fields

from config import db, ma


class Feature(db.Model):
    __tablename__ = "Feature"
    Feature_ID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    Feature_Name = db.Column(db.String, nullable=False)
    Trail_ID = db.Column(db.Integer, db.ForeignKey("Trail.Trail_ID"))


class FeatureSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Feature
        load_instance = True
        sql_session = db.session
        include_fk = True

class TrailUser(db.Model):
    __tablename__ = "TrailUser"
    UserID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    UserName = db.Column(db.String (50), nullable = False, unique = True)
    Email_address = db.Column(db.String (50), nullable = False, unique = True)
    UserRole = db.Column(db.String (20), nullable = False)

class TrailUserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = TrailUser
        load_instance = True
        sql_session = db.session

class Trail(db.Model):
    __tablename__ = "Trail"
    Trail_ID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    Trail_Name = db.Column(db.String (50), nullable = False)
    Trail_Location = db.Column(db.String (100))
    Trail_Rating = db.Column(db.Float)
    Trail_Difficulty = db.Column(db.String (20))
    Trail_Length_KM  = db.Column(db.Integer)
    Trail_Elevation_Gain_M = db.Column(db.Integer)
    Trail_Route_Type = db.Column(db.String (20))
    Trail_Estimated_Finish_Time_Min = db.Column(db.Integer)
    Trail_Summary = db.Column(db.String (1500))
    Trail_Description = db.Column(db.String (2000))
    Email_address = db.Column(db.String (50), db.ForeignKey("TrailUser.Email_address"), nullable = False)
    Point1_lat = db.Column(db.Float)
    Point1_long = db.Column(db.Float)
    Point1_Desc = db.Column(db.String (30))
    Point2_lat = db.Column(db.Float)
    Point2_long = db.Column(db.Float)
    Point2_Desc = db.Column(db.String (30))
    Point3_lat = db.Column(db.Float)
    Point3_long = db.Column(db.Float)
    Point3_Desc = db.Column(db.String (30))
    Point4_lat = db.Column(db.Float)
    Point4_long = db.Column(db.Float)
    Point4_Desc = db.Column(db.String (30))
    Point5_lat = db.Column(db.Float)
    Point5_long = db.Column(db.Float)
    Point5_Desc = db.Column(db.String (30))
    Features = db.relationship(
        Feature,
        backref="Trail",
        cascade="all, delete, delete-orphan",
        single_parent=True,
        order_by="Feature.Feature_Name"
    )

class TrailSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Trail
        load_instance = True
        sql_session = db.session
        include_relationships = True
        include_fk = True

    Features = fields.Nested(FeatureSchema, many=True)


feature_schema = FeatureSchema()
trail_user_schema = TrailUserSchema()

trail_schema = TrailSchema()
trails_schema = TrailSchema(many=True)
