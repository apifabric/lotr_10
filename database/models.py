# coding: utf-8
from sqlalchemy import DECIMAL, DateTime  # API Logic Server GenAI assist
from sqlalchemy import Column, DateTime, Float, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

########################################################################################################################
# Classes describing database for SqlAlchemy ORM, initially created by schema introspection.
#
# Alter this file per your database maintenance policy
#    See https://apilogicserver.github.io/Docs/Project-Rebuild/#rebuilding
#
# Created:  October 30, 2024 08:48:16
# Database: sqlite:////tmp/tmp.PXkK3USh8Q/lotr_10/database/db.sqlite
# Dialect:  sqlite
#
# mypy: ignore-errors
########################################################################################################################
 
from database.system.SAFRSBaseX import SAFRSBaseX
from flask_login import UserMixin
import safrs, flask_sqlalchemy
from safrs import jsonapi_attr
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship
from sqlalchemy.orm import Mapped
from sqlalchemy.sql.sqltypes import NullType
from typing import List

db = SQLAlchemy() 
Base = declarative_base()  # type: flask_sqlalchemy.model.DefaultMeta
metadata = Base.metadata

#NullType = db.String  # datatype fixup
#TIMESTAMP= db.TIMESTAMP

from sqlalchemy.dialects.sqlite import *



class Attraction(SAFRSBaseX, Base):
    """
    description: Table to describe various attractions within the park.
    """
    __tablename__ = 'attractions'
    _s_collection_name = 'Attraction'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    theme = Column(String)

    # parent relationships (access parent)

    # child relationships (access children)



class Event(SAFRSBaseX, Base):
    """
    description: Table for scheduled events at the theme park.
    """
    __tablename__ = 'events'
    _s_collection_name = 'Event'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    date = Column(DateTime)

    # parent relationships (access parent)

    # child relationships (access children)



class FoodAndBeverage(SAFRSBaseX, Base):
    """
    description: Table for food and beverage outlets.
    """
    __tablename__ = 'food_and_beverage'
    _s_collection_name = 'FoodAndBeverage'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    menu_type = Column(String)

    # parent relationships (access parent)

    # child relationships (access children)



class Map(SAFRSBaseX, Base):
    """
    description: Table for park maps.
    """
    __tablename__ = 'maps'
    _s_collection_name = 'Map'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    version = Column(String)
    release_date = Column(DateTime)

    # parent relationships (access parent)

    # child relationships (access children)



class Merchandise(SAFRSBaseX, Base):
    """
    description: Table detailing merchandise available in the park.
    """
    __tablename__ = 'merchandise'
    _s_collection_name = 'Merchandise'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    price = Column(Float)

    # parent relationships (access parent)

    # child relationships (access children)



class Ride(SAFRSBaseX, Base):
    """
    description: Table to store theme park rides information.
    """
    __tablename__ = 'rides'
    _s_collection_name = 'Ride'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    min_height_cm = Column(Integer)
    intensity_level = Column(Integer)

    # parent relationships (access parent)

    # child relationships (access children)
    MaintenanceScheduleList : Mapped[List["MaintenanceSchedule"]] = relationship(back_populates="ride")
    TicketList : Mapped[List["Ticket"]] = relationship(back_populates="ride")



class Staff(SAFRSBaseX, Base):
    """
    description: Table to track park staff details.
    """
    __tablename__ = 'staff'
    _s_collection_name = 'Staff'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    role = Column(String)

    # parent relationships (access parent)

    # child relationships (access children)



class Visitor(SAFRSBaseX, Base):
    """
    description: Table to store visitors' data.
    """
    __tablename__ = 'visitors'
    _s_collection_name = 'Visitor'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)
    email = Column(String)

    # parent relationships (access parent)

    # child relationships (access children)
    FeedbackList : Mapped[List["Feedback"]] = relationship(back_populates="visitor")
    MembershipList : Mapped[List["Membership"]] = relationship(back_populates="visitor")
    TicketList : Mapped[List["Ticket"]] = relationship(back_populates="visitor")



class Feedback(SAFRSBaseX, Base):
    """
    description: Table for collecting visitor feedback.
    """
    __tablename__ = 'feedback'
    _s_collection_name = 'Feedback'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    visitor_id = Column(ForeignKey('visitors.id'))
    comments = Column(String)

    # parent relationships (access parent)
    visitor : Mapped["Visitor"] = relationship(back_populates=("FeedbackList"))

    # child relationships (access children)



class MaintenanceSchedule(SAFRSBaseX, Base):
    """
    description: Table to manage ride maintenance schedules.
    """
    __tablename__ = 'maintenance_schedule'
    _s_collection_name = 'MaintenanceSchedule'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    ride_id = Column(ForeignKey('rides.id'))
    date_scheduled = Column(DateTime)

    # parent relationships (access parent)
    ride : Mapped["Ride"] = relationship(back_populates=("MaintenanceScheduleList"))

    # child relationships (access children)



class Membership(SAFRSBaseX, Base):
    """
    description: Table that manages visitor memberships.
    """
    __tablename__ = 'memberships'
    _s_collection_name = 'Membership'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    visitor_id = Column(ForeignKey('visitors.id'))
    membership_type = Column(String)
    expiry_date = Column(DateTime)

    # parent relationships (access parent)
    visitor : Mapped["Visitor"] = relationship(back_populates=("MembershipList"))

    # child relationships (access children)



class Ticket(SAFRSBaseX, Base):
    """
    description: Table for recording park ticket sales.
    """
    __tablename__ = 'tickets'
    _s_collection_name = 'Ticket'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    visitor_id = Column(ForeignKey('visitors.id'))
    ride_id = Column(ForeignKey('rides.id'))
    purchase_date = Column(DateTime)

    # parent relationships (access parent)
    ride : Mapped["Ride"] = relationship(back_populates=("TicketList"))
    visitor : Mapped["Visitor"] = relationship(back_populates=("TicketList"))

    # child relationships (access children)
