import datetime

from flask_appbuilder import Model
from sqlalchemy import Column, Date, Integer, String,Float

def today():
    return datetime.datetime.today().strftime("%Y-%m-%d")

class Cislo(Model):
    id = Column(Integer, primary_key=True)
    cislo = Column(Float, nullable=False)

    def __repr__(self, min=-5.01, max=4.99, message="zadej jine cislo"):
        return self.cislo