# Import from peewee
from peewee import *

# Connect to the SQLite database
db = SqliteDatabase('EV_Comparator.db')

# Define what a 'Vehicle' is
class Vehicle(Model):
  # These are all the fields it has
  # match up CharField/IntegerField/etc with correct type
  a = FloatField(primary_key=True) # primary key = unique id
  gallons = FloatField()
  city_mpg = FloatField()
  avg_mpg = FloatField()
  highway_mpg = FloatField()
  make = CharField()
  model = CharField()
  year = FloatField()

  class Meta:
    # data is coming from schools.db
    database = db
    # and it's in the table called 'schools'
    db_table = 'vehicles'

# Repeat with the energy scores
class Energy(Model):
  dbn = CharField(primary_key=True)
  school_name = CharField()
  number_of_test_takers = CharField()
  critical_reading_mean = IntegerField()
  mathematics_mean = IntegerField()
  writing_mean = IntegerField()
  
  class Meta:
    database = db
    db_table = 'energy'